def cubeCount(line:str, r_max: int, g_max: int, b_max: int, part: int):
   cube_counter = {'red': 0, 'green': 0, 'blue': 0}

   # Find the largest number of each colour cube
   round_list = line[line.index(':') + 2:].split('; ')
   
   for round in round_list:
      for colour in round.split(', '):
         if 'red' in colour:
            num = int(colour[0: -4])
            if num > cube_counter['red']:
               cube_counter['red'] = num
         
         elif 'green' in colour:
            num = int(colour[0: -6])
            if num > cube_counter['green']:
               cube_counter['green'] = num

         elif 'blue' in colour:
            num = int(colour[0: -5])
            if num > cube_counter['blue']:
               cube_counter['blue'] = num
   
   # Get game number
   game_number = int(line[5: line.index(':')])
      
   if part == 1:
      if (cube_counter['red'] > r_max) or (cube_counter['green'] > g_max) or (cube_counter['blue'] > b_max):
         return 0
   
      else:
         return game_number
   else:
      game_power = cube_counter['red'] * cube_counter['green'] * cube_counter['blue']
      return game_power


def main():
   fin = open("input2.txt")
   part = 1 # part of the task we wish to observe (1 or 2)

   # Maximum number of each colour cubes allowed
   r_max = 12 
   g_max = 13 
   b_max = 14

   game_sum = 0
   for line in fin.readlines():
      line = line.strip()
      game_sum += cubeCount(line, r_max, g_max, b_max, part=part)

   print(game_sum)



if __name__ == '__main__':
   main()