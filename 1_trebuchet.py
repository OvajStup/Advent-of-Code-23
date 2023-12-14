global numbers 
numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def getLineSum(line: str):
   num_indexes = {}

   # Check for direct integers
   for i in range(len(line)):
      if line[i] in '1 2 3 4 5 6 7 8 9':
         num_indexes[i] = int(line[i])         
   
   # Check for word integers
   for number in numbers.keys():
      if number in line:
         for i in range(len(line)):
            if line[i: len(number) + i] == number:
               num_indexes[i] = numbers[number]

   # Find first and last digits
   dig1 = str(num_indexes[min(num_indexes.keys())])
   dig2 = str(num_indexes[max(num_indexes.keys())])

   return int(dig1 + dig2)


def main():
   fin = open("D:\Programi\Python\Advent of Code_2023\input1.txt")
   
   total_sum = 0
   for line in fin.readlines():
      total_sum += getLineSum(line)

   print(total_sum)




if __name__ == '__main__':
   main()