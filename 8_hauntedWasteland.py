from math import lcm

def initializeMap(lines):
    """
    Initialize map dictionary from input file.
    """
    # Get list of directions
    directions = lines[0].strip()
    
    # Get map dictionary
    map_dict = {}
    for line in lines[2:]:
        split_line = line.split(' = ')
        map_dict[split_line[0]] = (split_line[1].strip()[1:-1].split(', '))
        
    return map_dict, directions


def initializeANodes(map_dict):
    """
    Find all nodes ending with 'A'.
    """
    aNodes = []
    for node in map_dict.keys():
        if node[-1] == 'A':
            aNodes.append(node)
    
    return aNodes


def getNodePeriod(node, map_dict, directions):
    """
    Find period for given node. A period is the number of steps after which the node repeats.
    """
    node_period = traverseMap(map_dict, directions, part=2, node=node)
    return node_period          
    

def traverseMap(map_dict, directions, part=1, node=None):
    """
    Follows directions from 'directions' list on the map, 'map_dict'.
    """
    counter = 0
    
    # Part-based variables
    if part == 1:
        pozition = 'AAA'
        end_pozition = 'ZZZ'
    
    else:
        pozition = node
    
    # Repeat instructions until end is found
    while (part == 1 and pozition != end_pozition) or (part == 2 and pozition[-1] != 'Z'):
        for direction in directions:
            # Left turn
            if direction == 'L':
                pozition = map_dict[pozition][0]
                counter += 1
                
            # Right turn
            else:
                pozition = map_dict[pozition][1]
                counter += 1
            
            # Check if end was found
            if (part == 1 and pozition == end_pozition) or (part == 2 and pozition[-1] == 'Z'):
                break         
        
    return counter
                
 
def main():
    fin = open(r"C:\Users\HP\OneDrive - fer.hr\UPRO\AoC\input8.txt")
    lines = fin.readlines()
    part = 2
    
    map_dict, directions = initializeMap(lines)
    
    if part == 1:
        steps = traverseMap(map_dict, directions)

    if part == 2:
        # Get periods of all nodes ending with 'A'
        aNodes = initializeANodes(map_dict)
        node_periods = [0 for i in range(len(aNodes))]
        for i in range(len(aNodes)):
            node_periods[i] = getNodePeriod(aNodes[i], map_dict, directions)
        
        # Find lowest common multiple of the periods (first place where all nodes end)
        node_periods = tuple(node_periods)
        steps = lcm(*node_periods)
        
    print(steps)
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
"""
        Brute force solution        
        while not allNodesFinished(aNodes):
            for direction in directions:
                if direction == 'L':
                    for node in range(len(aNodes)):
                        aNodes[node] = map_dict[aNodes[node]][0]
                    counter += 1
                    
                else:
                    for node in range(len(aNodes)):
                        aNodes[node] = map_dict[aNodes[node]][1]
                    counter += 1
            
                if allNodesFinished(aNodes):
                    break
        """