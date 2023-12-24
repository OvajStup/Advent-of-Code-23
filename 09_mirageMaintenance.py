def initializeHistories(lines):
   """
   Initializes list of histories from input file
   """
   histories = []
   for line in lines:
      line = line.strip().split(' ')
      histories.append([int(num) for num in line])
   
   return histories


def generateSequences(sequence):
   """
   Generates a reverse Pascal's triangle from a given sequence.
   """
   # End if the final sequence has been reached
   if sequence == [0 for i in range(len(sequence))]:
      return
   
   # Append next sequence level to the global list and continue
   else:
      seq = []
      for i in range(len(sequence) - 1):
         seq.append(sequence[i + 1] - sequence[i])
      sequences.append(seq)
      generateSequences(seq)


def extrapolate(sequences):
   """
   Updates 'sequences' with predicted values.
   """
   sequences[-1].append(0)
   for i in range(len(sequences) - 2, -1, -1):
      sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])

   return sequences


def extrapolateBackwards(sequences):
   """
   Updates 'sequences' with predicted values (backwards)
   """
   sequences[-1] = [0] + sequences[-1]
   for i in range(len(sequences) - 2, -1, -1):
      sequences[i] = [sequences[i][0] - sequences[i + 1][0]] + sequences[i]

   return sequences


def main():
   fin = open("input9.txt")
   lines = fin.readlines()
   part = 2
   global sequences

   history_sum = 0
   histories = initializeHistories(lines)

   for history in histories:
      sequences = [history]
      generateSequences(history)
      # Extrapolate next value
      if part == 1:
         sequences = extrapolate(sequences)
         history_sum += sequences[0][-1] 
      
      # Extrapolate value before the first 
      elif part == 2:
         sequences = extrapolateBackwards(sequences)
         history_sum += sequences[0][0]

   print(history_sum)



if __name__ == '__main__':
   main()