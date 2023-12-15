def isNumber (s: str):
   """
   Checks if a character is a digit.
   """
   if ord(s) in range(48, 58):
      return True
   else:
      return False
   

def isCharacter(s: str):
   """
   Checks if a character is a special symbol.
   """
   if s != '.' and not isNumber(s):
      return True
   else:
      return False
   
   
def isPart(row, col, engine_matrix):
   """
   Checks if a number is an engine part.
   """
   part = False
   char = engine_matrix[row][col]

   # Check vicinity of given coordinate
   for i in range(row - 1, row + 2):
      if part:
         break

      for j in range(col - 1, col + 2):
         if i < 0 or j < 0 or i > len(engine_matrix) - 1 or j > len(engine_matrix[i]) - 1:
            continue
         
         # Add coordinate to list of found asterisks
         if isCharacter(engine_matrix[i][j]):
            if engine_matrix[i][j] == '*':
               asterisks.add((i, j))

            part = True
            break
   
   return part


def processGears(engine_matrix):
   """
   Iterates through the list of found asterisks and adds gears to the gear dictionary.
   """
   for ast in asterisks:
      # Check vicinity for numbers
      for i in range(int(ast[0]) - 1, int(ast[0]) + 2):
         len_to_skip = 0
         for j in range(int(ast[1]) - 1, int(ast[1]) + 2):
            if not len_to_skip:
               if i < 0 or j < 0 or i > len(engine_matrix) - 1 or j > len(engine_matrix[i]) - 1:
                  continue

               if isNumber(engine_matrix[i][j]):
                  # check left
                  num = engine_matrix[i][j]
                  
                  q = j - 1;
                  while q >= 0 and isNumber(engine_matrix[i][q]):
                     num = engine_matrix[i][q] + num
                     q -= 1

                  # check right
                  q = j + 1;
                  while q <= len(engine_matrix[i]) - 1 and isNumber(engine_matrix[i][q]):
                     num = num + engine_matrix[i][q]
                     len_to_skip += 1
                     q += 1
               
                  # add nums to gear dictionary
                  if ast in gears.keys():
                     gears[ast].append(num)
                  else:
                     gears[ast] = [num]
            else:
               len_to_skip -= 1

               
def findGears(engine_matrix):
   """
   Calculates gear product for each actual gear.
   """
   processGears(engine_matrix)
   gear_product = 0
 
   for gear in gears:
      if len(gears[gear]) == 2:
         gear_product += int(gears[gear][0]) * int(gears[gear][1])

   return gear_product


def engine(engine_matrix: list):
   number_dict = {}
   part_sum = 0
   
   # line preprocessing
   for line in range(len(engine_matrix)):
      engine_matrix[line] = engine_matrix[line].strip()

   # find numbers in each line
   len_to_skip = 0
   for i in range(len(engine_matrix)):
      for j in range(len(engine_matrix[i])):
         if not len_to_skip:
            c = j; part = False
            try:
               isNumber(engine_matrix[i][c]) and c < len(engine_matrix)
            except:
               print(f"i = {i}, j = {j}, c = {c}")

            while c < len(engine_matrix[i]) and isNumber(engine_matrix[i][c]):
               
               # adding number to dict
               if (i, j) in number_dict.keys():
                  number_dict[(i, j)] += engine_matrix[i][c]
                  len_to_skip += 1
               else:
                  number_dict[(i, j)] = engine_matrix[i][c]
                  len_to_skip += 1

               if not part:
                  part = isPart(i, c, engine_matrix)
               c += 1

            if part:
               part_sum += int(number_dict[(i, j)])
         
         else:
            len_to_skip -= 1

   return part_sum, findGears(engine_matrix)


def main():
   fin = open('D:\Programi\Python\Advent of Code_2023\input3.txt')

   global blueprint, gears, asterisks
   blueprint = fin.readlines()
   gears = {}
   asterisks = set()
   
   part_sum, product_sum = engine(blueprint)
   print(f'part sum: {part_sum}')
   print(f'product sum: {product_sum}')


if __name__ == '__main__':
   main()
