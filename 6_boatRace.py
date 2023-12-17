def finProcessing(fin, part):
   """
   Converts input file into usable form depending on task part.
   """
   # Variable formatting
   lines = fin.readlines()
   races = []
   
   time = lines[0][9:].strip().split(' ')
   time = [t.strip() for t in time]
   
   records = lines[1][9:].strip().split(' ')
   records = [record.strip() for record in records]
   
   # Remove unnecessary bits left over from splitting and such
   for item in range(len(time) - 1, -1, -1):
      if time[item] == '':
         del(time[item])
      else:
         time[item] = int(time[item])

   for item in range(len(records) - 1, -1, -1):
      if records[item] == '':
         del(records[item])   
      else:
         records[item] = int(records[item])

   # Generation of "races" list
   if part == 1:
      # Add all races to list
      for item in range(len(time)):
         races.append((time[item], records[item]))
   
   elif part == 2:
      # Concatenate all data to get one big race
      time_act = ''
      for t in time:
         time_act += str(t)
      
      record_act = ''
      for r in records:
         record_act += str(r)
      
      races.append((int(time_act), int(record_act)))

   return races


def raceVariations(races):
   """
   Finds all possible winning variations for each race and multiplies them.
   """
   race_variations = []
   # Find winning variations
   for race in races:
      counter = 0
      time = race[0]
      record = race[1]
      
      for vel in range(time):
         if vel * (time - vel) > record: 
            counter += 1
      
      race_variations.append(counter)
   
   # Generate race product
   product = 1
   for race in race_variations:
      product *= race

   return product


def main():
   fin = open('input6.txt')
   part = 2

   races = finProcessing(fin, part)
   race_product = raceVariations(races)

   print(race_product)




if __name__ == '__main__':
   main()
