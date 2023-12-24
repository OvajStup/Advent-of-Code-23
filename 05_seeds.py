def seedToEnd(thing, maps, map_list, index=0):
   """
   Converts seed through all given maps and returns the final value.
   """
   # Look for applicable condition
   for record in range(len(maps[map_list[index]])):
      source_start = maps[map_list[index]][record][1]
      dest_start = maps[map_list[index]][record][0]
      range_len = maps[map_list[index]][record][2]

      # If applicable condition was found
      if thing in range(source_start, source_start + range_len + 1):
         next_thing = dest_start + (thing - source_start)
         
         # If this is the last map 
         if index == len(map_list) - 1:
            return next_thing
         
         # Continue conversions
         else:
            return seedToEnd(next_thing, maps, map_list, index + 1)
   
   # If no condition was found and this is the last map
   if index == len(map_list) - 1:
      return thing
   
   # If no condition was found 
   else:
      return seedToEnd(thing, maps, map_list, index + 1)
         
      
def initializeMaps(lines):
   """
   Initializes maps into dictionaries as well as a support list.
   """
   maps = {}; map_list = []
   for i in range(len(lines)):
      # Get map names
      if 'map' in lines[i]:
         current = f'{lines[i].split(" ")[0]}'
         maps[current] = []
         map_list.append(current)
      
      # Get map values
      else:
         if lines[i] != '\n':
            current_line = lines[i].split(' ')
            for number in range(len(current_line)):
               current_line[number] = int(current_line[number])
            maps[map_list[-1]].append(current_line)

   return maps, map_list
      

def endToSeed(thing, maps, map_list, index):
   """
   Inverse of seed_to_end. Finds seed for a given location.
   """
   # Look for applicable condition
   for record in range(len(maps[map_list[index]])):
      source_start = maps[map_list[index]][record][1]
      dest_start = maps[map_list[index]][record][0]
      range_len = maps[map_list[index]][record][2]

      # If applicable condition was found
      if thing in range(dest_start, dest_start + range_len + 1):
         next_thing = source_start + (thing - dest_start)
         
         # If this is the last map 
         if index == 0:
            return next_thing
         
         # Else, continue conversions
         else:
            return endToSeed(next_thing, maps, map_list, index - 1)

   # If no condition was found and this is the last map
   if index == 0:
      return thing
   
   # If no condition was found
   else:
      return endToSeed(thing, maps, map_list, index - 1)


def main():
   fin = open('input5.txt')
   part = 2

   lines = fin.readlines()
   maps, map_list = initializeMaps(lines[2:])

   if part == 1:
      seeds = lines[0][7:].strip().split(' ')
      seeds = [int(seeds[seed]) for seed in range(len(seeds))]
      locations = []
      
      # Find lowest location among given seeds
      for seed in seeds:
         location = seedToEnd(seed, maps, map_list)
         locations.append(location)

      print(min(locations))
   
   elif part == 2:
      # Find lowest location among given seed ranges
      initial_seeds = lines[0][7:].strip().split(' ')
      initial_seeds = [int(initial_seeds[seed]) for seed in range(len(initial_seeds))]
      borders = []
      
      # Find lowest location on seed range boundaries
      for seed in range(0, len(initial_seeds), 2):
         lower_bound = seedToEnd(initial_seeds[seed], maps, map_list)
         upper_bound = seedToEnd(initial_seeds[seed] + initial_seeds[seed + 1], maps, map_list)
         borders.append((lower_bound, upper_bound))

      # Find lowest location among these boundaries
      min_member = (0, 0)
      for i in range(len(borders)):
         for j in range(2):
            if borders[i][j] < borders[min_member[0]][min_member[1]]:
               min_member = (i, j)
      
      # Starting from found lowest location, check if any lower exist 
      # (not optimal, would be better to start from 0 and go upwards)
      comparisons = []
      for i in range(0, len(initial_seeds), 2):
         comparisons.append(initial_seeds[i])
         comparisons.append(initial_seeds[i] + initial_seeds[i + 1])

      min_location = borders[min_member[0]][min_member[1]]
      for loc in range(min_location, -1, -1):
         seed = endToSeed(loc, maps, map_list, len(map_list) - 1)
         
         # Compare found seed to initial seed ranges
         for initial_s in range(0, len(initial_seeds), 2):
            if seed >= comparisons[initial_s] and seed <= comparisons[initial_s + 1]:
               min_location = loc

         # Progress check to make sure program is still alive
         if loc % 1000000 == 0:
            print(loc)

         print(min_location)
 


if __name__ == '__main__':
   main()

   