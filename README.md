# RoboticPathfinderAlgo
Robotic Pathfinder implementation of depth first search algorithm and uniform cost search algorithm


This code implements two simple pathfinding algorithms; depth first search & uniform cost search.

The code is meant to take in a 2D model of a grid world (based on amazon warehouse robotic environment). 

The code can only accept 2D grid enviroments in .txt form

The .txt 2D enviroments have the following symbols:

"@" => robot or agent
"_" => empty space that the robot can traverse
"*" => Goal, this could be a package that the robot needs to pick up. NOTE: there can be any number of goals/packages in the 2D environment
"#" => Obstacle that the robot cannot pass. The robot must find a path around obstacles

Included in the repo are .txt files that represent 2D enviroments.

The code can be run on the command line and accepts two arguments:

Argument #1: "dfs" or "ucs", this designates the type of algorithm being used to find the optimal path. Obviously, uniform cost search will be more efficient since it has a heuristic guiding the robot.

Argument #2: Filepath to 2D enviroment being explored. This must be a .txt file in the previously mentioned format. 

The code will then return a path as a series of directions. The directions are limited to the four cardinal directions (up, down, left, right).

The directions are shortened to "U" = up, "D" = down, "L" = left, "R" = right

Also included in the path will be the direction marked "S". This stands for "Sample" meaning that the robot has reached a desired goal/package.

Originally, these algorithms were used as a hypothetical application for the NASA moon rover, which would "Sample" mineral deposits on the surface of the moon.

In the case of the amazon warehouse enrivonment, sample is synonomous with "pickup/dropoff" a amazon package.

The repo includes 6 different 2D environments in .txt file format that the user can apply to the code. 

The code will also report the amount of "expanded nodes" and the amount of "generated nodes".

Exanded nodes are the amount of nodes that the algorithm has explored whereas the generated nodes are the total amount of nodes that the algorithm has generated hypothetically, but hasn't necessary explored. 

