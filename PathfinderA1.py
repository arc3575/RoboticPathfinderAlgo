#Import necessary libraries
import numpy as np
import sys

#COMMAND LINE ARGUMENTS

#Make sure there are the correct amount of arguments in command line

if len(sys.argv) !=3:
    print("python SampleWorld.py <algoType> <input_file>")
    sys.exit(1)
#Algo type is dfs or ucs

algoType = sys.argv[1].lower()
file_path1 = sys.argv[2]


#TUPLE METHOD
def tup(tuple_of_arrays):
    tuple_of_ints = tuple(int(arr[0]) if isinstance(arr, (list, np.ndarray)) and len(arr) > 0 else None for arr in tuple_of_arrays)
    return tuple_of_ints


#READS in text file

def read_txt_to_numpy_string(file_path):

    try:
        with open(file_path, 'r') as file:
            lines = [line.rstrip('\n') for line in file]
        return np.array(lines, dtype=str)
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'.")
        return np.array([])
    except Exception as e:
         print(f"An error occurred: {e}")
         return np.array([])


def convert_string_array_to_numeric_array(arr, conversion_rules): 
    #Default empty as float
    new_arr = np.empty_like(arr, dtype=float) 
    #loop go through rows
    for i in range(arr.shape[0]):
    #Loop go through columns
        for j in range(arr.shape[1]):
            #get value from old array
            val = arr[i, j]
            #Use value from old array to define value of new array
            if val in conversion_rules:
                new_arr[i, j] = conversion_rules[val]
            #Error if not possible
            else:
                try:
                    new_arr[i, j] = float(val)
                except ValueError:
                    print(f"Error: Could not convert '{val}' at position ({i}, {j}) to a number and no default rule was provided.")
                    return None  
    return new_arr


#EXPAND METHOD

def expand(parent, grid, visited):

    i = parent[0]
    j = parent[1]
    shp = grid.shape
    downLim = shp[0]
    rightLim = shp[1]
    #Four cardinal positions
    nodeUp = (i - 1, j)
    nodeDown = (i + 1, j)
    nodeRight = (i, j + 1)
    nodeLeft = (i, j -1)
    #Up
    #conditional that specifies that the moved to location is not off grid
    #and the moved to location is not a barrier, which is represented by a 3 
    nodeArray = []
    if ((i - 1) >= 0) and (grid[i-1, j] != 3) and (nodeUp not in visited):
        nodeArray.append(nodeUp)
    #Down
    if ((i + 1) < downLim) and (grid[i + 1, j] != 3) and (tuple((i + 1, j)) not in visited):
        nodeArray.append(nodeDown)
    #Right
    if ((j + 1) < rightLim) and (grid[i, j + 1] != 3) and (nodeRight not in visited):
        nodeArray.append(nodeRight)
    #Left
    if ((j - 1) >= 0) and (grid[i, j - 1] != 3) and (nodeLeft not in visited):
        nodeArray.append(nodeLeft)
    #Sample
    # if grid[i , j] == 2:
    #     nodeSample = (-1, -1)
    #     nodeArray.append(nodeSample)

    return nodeArray

#DIRECTION METHOD

def direction(previousNode, Node):
    result_tuple = tuple(j - i for i, j in zip(previousNode, Node))

    if result_tuple == (0, 1):
        return "R"
    if result_tuple == (0, -1):
        return "L"
    if result_tuple == (-1, 0):
        return "U"
    if result_tuple == (1, 0):
        return "D"


#Dictionaries used in backtracking

#Used in backtracking

reverse = {"R": "L", "L": "R" , "U": "D", "D": "U"}
unitVectors = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0,-1)}

#DEPTH FIRST SEARCH

def depthFirstSearch(grid, startNode):
    totalSample = len(np.argwhere(grid == 2))
    sampleCounter = 0
    stack = [startNode]
    pathList = []
    visited = {}
    node = startNode
    expandedNodeCounter = 0
    generatedNodeCounter = 0
    while True:
        if len(stack) == 0:
            return "Failure" , generatedNodeCounter, expandedNodeCounter
        previousNode = node
        node = stack.pop()
        if previousNode != node:
            pathList.append(direction(previousNode, node))
        visited[node] = True
        if grid[node] == 2:
            grid[node] = 0
            pathList.append("S")
            sampleCounter += 1
        if sampleCounter == totalSample:
            return pathList, generatedNodeCounter, expandedNodeCounter
        else:
            
            children = expand(node, grid, visited)
            generatedNodeCounter += len(children)
            expandedNodeCounter += 1
            childrenUnique = [node for node in children if node not in stack]
            if len(childrenUnique) == 0:
                #In case of backtracking
                backSteps = 0
                backPath = []
                branch = False
                while (not branch):
                    backSteps -= 1
                    previousStep = pathList[backSteps]
                    if previousStep == "S":
                        continue 
                    #In case the previous step is not sample, then backtrack
                    
                    reverseStep = reverse[previousStep]
                    backPath.append(reverseStep)
                    reverseDirection = unitVectors[reverseStep]
                    reverseNode = tuple(x + y for x, y in zip(node, reverseDirection))
                    #As long as you don't have children, branch equals False and the while loop will continue
                    #looking for if stack[-1] is in the children of the reverseNode
                    #This will tell you if one of the adjacent nodes is the last one on the stack, thus backtracking
                    branch = (stack[-1] in expand(reverseNode, grid, visited))
                    node = reverseNode
                pathList.extend(backPath)
                node = reverseNode

                    # reverseDirection = unitVectors[reverseStep]
                    # reverseNode = tuple(x + y for x, y in zip(node, reverseDirection))
                    # stack.append(reverseNode)
                    
            else:

                #Children that are NOT already on stack
                stack.extend(childrenUnique)
                
                # if (len(stack) == 0) or((stack[-1] not in children)):
                    # stack.extend(children)

#UNIFORM COST SEARCH

#Similar to depth first search, but utilizes cost

def uniformCostSearch(grid, startNode):
    totalSample = len(np.argwhere(grid == 2))
    sampleCounter = 0
    stack = [startNode]
    pathList = []
    visited = {}
    node = startNode
    total_loop = 0
    expandedNodeCounter = 0
    generatedNodeCounter = 0
    while True:
        if len(stack) == 0:
            return "Failure", generatedNodeCounter, expandedNodeCounter
        previousNode = node
        node = stack.pop()
        if previousNode != node:
            pathList.append(direction(previousNode, node))
        visited[node] = True
        if grid[node] == 2:
            grid[node] = 0
            pathList.append("S")
            sampleCounter += 1
        if sampleCounter == totalSample:
            return pathList, generatedNodeCounter, expandedNodeCounter
        else:
            children = expand(node, grid, visited)
            generatedNodeCounter += len(children)
            expandedNodeCounter += 1
            childrenUnique = [node for node in children if node not in stack]
            if len(childrenUnique) == 0:
                #In case of backtracking
                backSteps = 0
                backPath = []
                branch = False
                while (not branch):
                    backSteps -= 1
                    previousStep = pathList[backSteps]
                    if previousStep == "S":
                        continue 
                    #In case the previous step is not sample, then backtrack    
                    reverseStep = reverse[previousStep]
                    backPath.append(reverseStep)
                    reverseDirection = unitVectors[reverseStep]
                    reverseNode = tuple(x + y for x, y in zip(node, reverseDirection))

                    #Same branching criteria as dfs
                    
                    branch = (stack[-1] in expand(reverseNode, grid, visited))
                    node = reverseNode
                pathList.extend(backPath)
                node = reverseNode

                    
            else:

                #Pass in Grid, when sampling, grid is updated so this will contain the closest goals
                #returns a 2D array with tuples and corresponding pathCost
                childrenCost = pathCost(childrenUnique, grid)

                #Sort array according to the 2nd column
                #Sort changes the list, sorted makes a copy and then stores it
                
                childrenCost.sort(key=lambda x: x[1], reverse = True)
                #Remove only the tuples, no costs
                
                childrenSorted = [row[0] for row in childrenCost]
                stack.extend(childrenSorted)
    


def pathCost(children, grid):

    goals = np.argwhere(grid == 2)
    costs = []
    for c in children:
        costsPerGoal = []
        for goal in goals:
            distance = ((goal[0] - c[0])**2 + (goal[1] - c[1])**2)**(1/2)
            costsPerGoal.append(distance)

        costsMin = min(costsPerGoal)
        costs.append((c, costsMin))

    return costs
#MAIN METHOD

def main(fp, at):
    file_path = fp
    algoType = at
    #Make an array of strings based on filepath
    string_array = read_txt_to_numpy_string(file_path)
    #Grab column and row
    column = string_array[0].astype(int)
    row = string_array[1].astype(int)

    #Delete column and row number from string array
    for i in range(2):
        string_array = np.delete(string_array, 0)


    char_array = np.array([list(string) for string in string_array])
    redim_array = np.resize(char_array, (row, column))

    #Conversion criteria to convert .txt into numpy array
    conversion_criteria = {'_': 0, "@":1, "*":2, "#":3}

    #Num array will be used as grid

    num_array = convert_string_array_to_numeric_array(redim_array, conversion_criteria)
    shp = num_array.shape
    startNode = np.where(num_array == 1)
    #VITAL step, converts startNode form an array of arrays into a tuple
    #Tuple is used to track the position of the agent, it also represents the nodes themselves
    
    startNode1 = tup(startNode)
    
    if algoType == "dfs":
        l1, g1, e1 = depthFirstSearch(num_array, startNode1)
    if algoType == "ucs":
        l1, g1, e1 = uniformCostSearch(num_array, startNode1)
    for i in l1:
        print(i)
    print(g1, " nodes generated")
    print(e1, " nodes expanded")
    
main(file_path1, algoType)
