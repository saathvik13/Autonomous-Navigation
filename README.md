B551 Assignment 0: Searching and Python 
Name- Sai Saathvik Domala

Part 1: Navigation

1) Abstractions

State Space – Set of all valid states of Pichu locations on given map with respect to    my location (‘@’) and walls (‘X’).

Initial States – The initial state is the given map with location of Pichu and my location (‘@’) before performing the search.

Successor Function – Set of actions Pichu can perform to reach my location. In this case it is ‘U’, ‘D’, ‘R’, ‘L’ from initial state to goal state.

Goal State – This is the state where the Pichu meets my location through the shortest path.

Cost Function – The cost function is same for all moves and it assumed to be 1.


2) Why does the program often fail to find a solution? Implement a fix to make the code work better and explain what you did in the report.
	
The given program fails to find the code as it tends to loop infinitely. This is because we do not keep track of the visited nodes. Moreover, the heuristic function as well as the search function are missing to guide Pichu to the Goal.
To overcome this problem, I created an empty list called ‘visited’ to keep track of all the neighbours my code has visited. If the code does not find a path, it returns ‘-1’.
Also, I implemented A- star search to find the shortest path. But I could not keep track of the path since A* search algorithm tends to jump around map depending as it picks the node with the lowest cost function. So, I used a function which uses backtracking to find the path from the goal to the start. Later, this path is passed to a function which gets the direction of moves, i.e.- ‘U’, ‘D’, ‘R’, ‘L’.

3) Overview

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


4) Problems you faced

	Initially I had used lists to work out the problem after checking many code blogs on the internet but few test cases did not pass. Moreover, I was not satisfied with the online code as I felt like I was almost copying the A* structure from another soruce. I, then, implemented a priority queue but I had the same issue. On Friday, I decided to start everything from scratch out of frustration and decided to use the concept of fringe. By far, this was the shortest and easiest method. I wish, I implemented it earlier. One of the main problems I was facing was getting the shortest path from the visited node. After trying many methods, I discussed with another classmate (who used the concept of fringe as well) and we both were able to narrow down a solid approach which uses backtracking. Basically, I implemented a function that backtracks from the Goal to the Start and only moves to the next node if the cost 1. Any other node with a difference of coordinates greater than 1 is ignored and the next node is considered. This way I was able to backtrack and find the shortest path.

Part 2: Hide and Seek

1) Abstractions

State Space – Set of all valid states of Pichu locations placed on given map where no other Pichu is visible row wise, column wise and diagonally.

Initial States – The initial state is the given map with location of 1 Pichu, my location (‘@’) and walls (‘X’) and no other Pichus on the map.

Successor Function – Set of actions where a Pichu can be placed on a ‘.’ such that it not in direct line of sight to another Pichu in the row, column, or diagonal. 

Goal State – This is the state where all the Pichus are arranged on the map such that they are not in direct line of sight with other.

Cost Function – The cost function is same for all moves and it assumed to be 1.

2) Overview
I have implemented the starter code given and my approach basically places a Pichu if the rows columns and diagonals are valid.

The algorithm is given below-

I.	Find the position of the initial Pichu

II.	Get the number of Pichus needed to be placed on the map.

III.	Initialise FRINGE with the initial configurations of the house map.

IV.	Find successors by traversing through every dot’.’ and check whether they are valid.

V.	Check whether a Pichu is in direct line of sight with another Pichu in the same row, column or diagonal and add if it satisfies the condition.

a.	Check if the insertion is inside the map

b.	Look ahead and behind from a Pichu to see if there any other Pichu in the row, column, or diagonal in direct line of contact.

VI.	If all the Pichus are inserted successfully, return then map. Else return False.

3) Problems you faced
	Initially, I tried implementing BFS using Queue, but I had many issues with that code and could not debug. I then stumbled upon a smarter approach of traversing forward and backward until it meets another Pichu or the wall. This took a long time to implement as I kept going back to my previous approach of using BFS with Queues.

4) Other Approaches

	An interesting approach I had was to place the pichu temporarily on the map, extract the rows, columns, and diagonals of that Pichu into a list. Then, I would remove all the dots’.’ in the list which would results in a list with ‘P’s and ‘X’s. If there exists two P’s together, it would return false. 








