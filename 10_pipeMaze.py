def mazeInitialization(lines):
   maze = []
   for line in lines:
      maze.append(line.strip())

   return maze


def findStart(maze):
   for i in range(len(maze)):
      for j in range(len(maze[i])):
         if maze[i][j] == 'S':
            return (i, j)
         

def polygonArea(vertices):
   poly_area = 0
   for x in range(len(vertices) - 1):
      height = ( (vertices[x][1]) + (vertices[x + 1][1])) / 2

      width = (vertices[x + 1][0]) - (vertices[x][0])
      if width < 0:
         width -= 1
         height += 1
      elif width == 0:
         pass
      else:
         width += 1

      area = width * height
      poly_area += area 

   return abs(poly_area)
    

def updatePosition(maze, i, j, prev_heading):
   current_square = maze[i][j]
   current_i = i; current_j = j

   # Vertical pipe
   if current_square == '|':
      if prev_heading == 'S':
         i += 1
         next_heading = 'S'
      elif prev_heading == 'N':
         i -= 1
         next_heading = 'N'
   
   # Horizontal pipe
   elif current_square == '-':
      if prev_heading == 'E':
         j += 1
         next_heading = 'E'

      elif prev_heading == 'W':
         j -= 1
         next_heading = 'W'

   # 90-degree bend (E-S)
   elif current_square == 'F':
      if prev_heading == 'N':
         j += 1
         next_heading = 'E'

      elif prev_heading == 'W':
         i += 1
         next_heading = 'S'

   # 90-degree bend (S-W)
   elif current_square == '7':
      if prev_heading == 'E':
         i += 1
         next_heading = 'S'
      
      elif prev_heading == 'N':
         j -= 1
         next_heading = 'W'

   # 90-degree bend (N-E)
   elif current_square == 'L':
      if prev_heading == 'S':
         j += 1
         next_heading = 'E'

      elif prev_heading == 'W':
         i -= 1
         next_heading = 'N'

   # 90-degree bend (N-W)
   elif current_square == 'J':
      if prev_heading == 'E':
         i -= 1
         next_heading = 'N'
      
      elif prev_heading == 'S':
         j -= 1
         next_heading = 'W'

   if prev_heading != next_heading:
      vertices.append((current_j, current_i))

   return i, j, next_heading
      
   
def findInitialDirection(maze, s_i, s_j):
   i, j = s_i, s_j
   if maze[s_i - 1][s_j] in '| F 7':
      prev_heading = 'N'
      i -= 1
      
   elif maze[s_i][s_j + 1] in '- J 7':
      prev_heading = 'E'
      j += 1

   elif maze[s_i + 1][s_j] in '| J L':
      prev_heading = 'S'
      i += 1
   
   elif maze[s_i] [s_j - 1] in '- L F':
      prev_heading = 'W'
      j -= 1

   return i, j, prev_heading


def traverseMap(maze):
   distances = [1]
   counter = 1
   s_i, s_j = findStart(maze)
   vertices.append((s_i, s_j))
   i, j, prev_heading = findInitialDirection(maze, s_i, s_j)   

   while (i != s_i) or (j != s_j):
      i, j, prev_heading = updatePosition(maze, i, j, prev_heading)
      if (i, j) != (s_i, s_j):
         counter += 1
         distances.append(counter)

   return distances


def main():
   fin = open('input10_test.txt')
   lines = fin.readlines()
   global vertices
   vertices = []
   part = 2

   maze = mazeInitialization(lines)

   # Find distance of point furthest from start
   clock_pass = traverseMap(maze)

   if part == 1:
      counter_clock_pass = clock_pass[::]

      counter_clock_pass.reverse()

      actual_dists = []
      for i in range(len(clock_pass)):
         actual_dists.append(min(clock_pass[i], counter_clock_pass[i]))

      print(max(actual_dists))

   # Experimental approach (unfinished, doesn't work)
   if part == 2:
      vertices.append(vertices[0])

      vertices = [(1, 1), (9, 1), (9, 7), (1, 7), (1, 1)]
      outer_area = polygonArea(vertices)
      inner_area = outer_area - (len(clock_pass) + 1)
      
      print(outer_area)
      print(len(clock_pass) + 1)
      print(inner_area)
      











if __name__ == '__main__':
   main()