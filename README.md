# Autonomous Navigation

### 1) Abstractions

#### State Space – Set of all valid states of Pichu locations on given map with respect to    my location (‘@’) and walls (‘X’).

#### Initial States – The initial state is the given map with location of Pichu and my location (‘@’) before performing the search.

#### Successor Function – Set of actions Pichu can perform to reach my location. In this case it is ‘U’, ‘D’, ‘R’, ‘L’ from initial state to goal state.

#### Goal State – This is the state where the Pichu meets my location through the shortest path.

#### Cost Function – The cost function is same for all moves and it assumed to be 1.


### 2) Why does the program often fail to find a solution? Implement a fix to make the code work better and explain what you did in the report.
	
The given program fails to find the code as it tends to loop infinitely. This is because we do not keep track of the visited nodes. Moreover, the heuristic function as well as the search function are missing to guide Pichu to the Goal.
To overcome this problem, I created an empty list called ‘visited’ to keep track of all the neighbours my code has visited. If the code does not find a path, it returns ‘-1’.
Also, I implemented A- star search to find the shortest path. But I could not keep track of the path since A* search algorithm tends to jump around map depending as it picks the node with the lowest cost function. So, I used a function which uses backtracking to find the path from the goal to the start. Later, this path is passed to a function which gets the direction of moves, i.e.- ‘U’, ‘D’, ‘R’, ‘L’.

### 3) Overview

My approach aligns with the starter code provided by Mr. David Crandall, and I have used the concept of fringe to solve this problem. Since the solution requires the shortest path, I chose A star as the algorithm.

The algorithm is given below –


I.	Find location of Pichu and Goal.

II.	Initialise a FRINGE with 3 values- Position, Current distance & Cost.

III.	Pop the node with the smallest cost value.

IV.	Find the neighbours and check if they are valid.

V.	Calculate the cost for the neighbour and add it to the fringe if it is not already visited.

VI.	Sort the fringe according to the lowest cost.

VII.	Run the search algorithm until it hits a goal, if it doesn’t reach the goal, return Failure.

VIII.	If the Goal is hit, find the shortest path using backtracking technique.

IX.	Find the Path string using the shortest path obtained.

X.	Return the Path length and the Path string








