def createUniverse(lines, part):
    """
    Initialize universe from input and expand it if necessary.
    """
    universe = [line.strip() for line in lines]
    empty_rows = set()
    empty_columns = set()

    # Expand rows
    for i in range(len(universe) - 1, -1, -1):
        try:
            # Attempt to find a galaxy in current line
            curr_index = universe[i].index('#')
        except ValueError:
            # Add blank rows after current index
            if part == 1:
                universe.insert(i + 1, universe[i])
            # Alternatively, add row index to set
            elif part == 2:
                empty_rows.add(i)
    
    # Expand columns
    for j in range(len(universe[0]) - 1, -1, -1):
        found = False
        for line in universe:
            if line[j] == '#':
                found = True
            
            if found:
                break

        if not found:
            # Add blank column after current index
            if part == 1:
                for i in range(len(universe) -1, -1, -1):
                    universe[i] = universe[i][:j + 1] + '.' + universe[i][j + 1:]
            
            # Alternatively, add column index to set
            elif part == 2:
                empty_columns.add(j)

    return universe, empty_rows, empty_columns



def findGalaxies(universe):
    """
    Returns list of all galaxy indices.s
    """
    galaxies = []
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == '#':
                galaxies.append((i, j))

    return galaxies


def findShortestPath(galaxy1:tuple, galaxy2:tuple) -> int:
    """
    Find the shortest path between two galaxies.
    The shortest path is simply the sum of the two galaxies' x and y coords.
    """
    path = abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
    return path


def getShortestPathSum(galaxies:list, empty_rows, empty_columns, part:int) -> int:
    """
    Returns the sum of the shortest paths between each pair of galaxies. 
    """
    shortest_path_sum = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            shortest_path_sum += findShortestPath(galaxies[i], galaxies[j])
            
            if part == 2:
                
                # Check if the path crosses any blank rows, which now have a size of 1 million
                x_1 = galaxies[i][0]
                x_2 = galaxies[j][0]
                for row in empty_rows:
                    if (x_1 > row and x_2 < row) or (x_1 < row and x_2 > row):
                        shortest_path_sum += 999999     # the blank row has already been traversed once in findShortestPath() 
                
                # Check if the path crosses any blank columns, which now have a size of 1 million
                y_1 = galaxies[i][1]
                y_2 = galaxies[j][1]
                for column in empty_columns:
                    if (y_1 > column and y_2 < column) or (y_1 < column and y_2 > column):
                        shortest_path_sum += 999999     # The blank column has already been traversed once in findShortestPath()

    return shortest_path_sum


def main():
    fin = open("input11.txt")
    lines = fin.readlines()
    part = 2

    expanded_universe, empty_rows, empty_columns = createUniverse(lines, part)
    galaxies = findGalaxies(expanded_universe)
    shortest_path_sum = getShortestPathSum(galaxies, empty_rows, empty_columns, part)

    print(shortest_path_sum)



if __name__ == '__main__':
    main()
    
    