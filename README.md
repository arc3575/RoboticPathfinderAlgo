# General overview of code
Robotic Pathfinder implementation of depth first search algorithm and uniform cost search algorithm


This code implements two simple pathfinding algorithms; depth first search & uniform cost search.

The code is meant to take in a 2D model of a grid world (based on amazon warehouse robotic environment). 

The code can only accept 2D grid enviroments in .txt form



# The .txt 2D enviroments have the following symbols:

"@" => robot or agent

"_" => empty space that the robot can traverse

"*" => Goal, this could be a package that the robot needs to pick up. NOTE: there can be any number of goals/packages in the 2D environment

"#" => Obstacle that the robot cannot pass. The robot must find a path around obstacles


# The code can be run on the command line and accepts two arguments:

Argument #1: "dfs" or "ucs", this designates the type of algorithm being used to find the optimal path. Obviously, uniform cost search will be more efficient since it has a heuristic guiding the robot.

Argument #2: Filepath to 2D enviroment being explored. This must be a .txt file in the previously mentioned format. 

# Returned path format

The code will then return a path as a series of directions. The directions are limited to the four cardinal directions (up, down, left, right).

The directions are shortened to "U" = up, "D" = down, "L" = left, "R" = right

Also included in the path will be the direction marked "S". This stands for "Sample" meaning that the robot has reached a desired goal/package.

Originally, these algorithms were used as a hypothetical application for the NASA moon rover, which would "Sample" mineral deposits on the surface of the moon.

In the case of the amazon warehouse enrivonment, sample is synonomous with "pickup/dropoff" a amazon package.

# Accompanying .txt files

The repo includes 11 different 2D environments in .txt file format that the user can apply to the code.

The following .txt files are stored in the folder labeled "warehouses". Each .txt file represents a 2D enviromenmt of a hypothetical warehouse model in varying sizes.

tiny1.txt

tiny2.txt

tiny3.txt 

tiny4.txt

small1.txt

small2.txt

small3.txt

medium1.txt

medium2.txt

large1.txt

large2.txt

# Explanation of Nodes

The code will also report the amount of "expanded nodes" and the amount of "generated nodes".

Exanded nodes are the amount of nodes that the algorithm has explored whereas the generated nodes are the total amount of nodes that the algorithm has generated hypothetically, but hasn't necessary explored. 

