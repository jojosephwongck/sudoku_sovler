def find_empty(matrix):
     for i in range(9):
          for j in range(9):
               # find the next empty slot, which is denoted by '.'
               if matrix[i][j] == '.':
                    return i , j
     return None, None

def check_valid(guess, row, col, matrix):
     if guess in matrix[row]:
          return False

     for i in range(9):
          if guess == matrix[i][col]:
               return False

     i = row // 3
     j = col // 3
     square = [matrix[3*i + a][3*j + b] for a in range(3) for b in range(3)]
     if guess in square:
          return False

     return True

def solver(matrix):
     row, col = find_empty(matrix)
     if row is None:
          return True

     for guess in range(1, 10):
          if check_valid(guess, row, col, matrix):
               matrix[row][col] = guess
               if solver(matrix):
                    return True
          matrix[row][col] = '.'

     return False

# Here's an example of solving a sodoku puzzle.
A = [[5, 3,".",".", 7,".",".",".","."],
     [6,".",".", 1, 9, 5,".",".","."],
     [".",9,8,".",".",".",".",6,"."],
     [8,".",".",".",6,".",".",".",3],
     [4,".",".",8,".",3,".",".",1],
     [7,".",".",".",2,".",".",".",6],
     [".",6,".",".",".",".",2,8,"."],
     [".",".",".",4,1,9,".",".",5],
     [".",".",".",".",8,".",".",7,9]]

solver(A)
for row in A:
     print(row)
