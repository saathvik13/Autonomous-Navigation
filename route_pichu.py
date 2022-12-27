#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [SAI SAATHVIK DOMALA, sdomala]
#
# Based on skeleton code provided in CSCI B551, Fall 2021.


import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

        # Return only moves that are within the house_map and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)


# Calculate the Heuristic function
def calculate_heuristic(me,move):
    # use Manhattan distance to find the heuristic distance
    return ( abs(me[0]-move[0]) + abs(me[1]-move[1]) )

# XX
# I interacted with another fellow student,Sravani Wayangankar, for a way to extract the shortest path from visited node and we both have implemented a similar approach.
# Using Backtracking technique to find the path from Goal to Start using the visited list
def find_path(visited):
    visited = [list(x) for x in visited]  # Convert the list of tuples to a list of list
    visited.reverse() # Reversing the string to traverse from Me(goal) to Pichu(start)

    # Using a stack to push the path-elements from the visited list and ignore the deviating visited nodes of A* Algorithm
    stack=[] # This stack is used to store the shortest path
    stack.append(visited[0])
    last=stack[-1] 
    
    # The for loop traverses through the visited node and it is compared to the last element of the stack, if the difference is 1, it will push the element of the visited node into the stack
    for i in range(len(visited)):
        if( abs(visited[i][0] - last[0]) + abs(visited[i][1] - last[1]) == 1 ): # Checks if the distance between consecutive nodes is 1, then appends to the stack
            stack.append(visited[i])
            last=stack[-1] # Updating last to the top of the stack so it can be used to compare to the visited list
    
    path = get_path(stack)
    return path # Gets the path in required format, ie- 'U', 'D', 'L', 'R'

# XX
#This function returns the path in the required format in form of a string
def get_path(stack):
    arrangement = [list(x) for x in stack] # Converting the arrangement to list of lists
    arrangement.reverse() #Reversing the list from start(Pichu) to goal(me)
    path_string=[] # This string stores the path of the sequence
    for i in range(len(arrangement)-1):
        if arrangement[i+1][0]-arrangement[i][0]==0 and arrangement[i+1][1]-arrangement[i][1]==1: # Checks if the next move is Right
            path_string.append("R")
        if arrangement[i+1][0]-arrangement[i][0]==1 and arrangement[i+1][1]-arrangement[i][1]==0: # Checks if the next move is Down
            path_string.append("D")
        if arrangement[i+1][0]-arrangement[i][0]==0 and arrangement[i+1][1]-arrangement[i][1]==-1: # Checks if the next move is Left
            path_string.append("L")
        if arrangement[i+1][0]-arrangement[i][0]==-1 and arrangement[i+1][1]-arrangement[i][1]==0: # Checks if the next move is Up
            path_string.append("U")
    return path_string

# Sorts the fringe in Ascending order according to the cost
def sort_acc_to_cost(fringe):
    return fringe[2]



def search(house_map):
    # Find pichu start position
    pichu = [(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i] == "p"][0] #Gets the position of Pichu
    me = [(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i] == "@"][0] #Gets my position

    move_string=[]

    visited=[pichu] #Storing visited with pichu as the first initialisation
    fringe=[(pichu,0,0)] 

    flag=0

    while len(fringe)>0:
        
        popped= (curr_move, curr_dist, cost) = fringe.pop(0) #Third variable in the fringe is used to store the cost of the current node

        for move in moves(house_map, *curr_move):
            if house_map[move[0]][move[1]] == "@": # Check if the current move is the Goal
                visited.append(move)

                move_string = find_path(visited)
                move_string = ''.join(move_string)
                move_count= len(move_string)
                
                flag = 1 

                return (move_count ,move_string)

            else:
                
                if move not in visited: #Check if the current node is already in visited
                    
                    visited.append(move)
                    
                    heuristic_cost = calculate_heuristic(me,move) # Calculate the heuristic from current node to the goal
                    
                    
                    cost = (curr_dist+1) + heuristic_cost #f(n)= g(n) + h(n) where cost is f(n), (current_distance+1) is g(n) and heuristic_cost is h(n)

                    fringe.append((move, curr_dist+1 ,cost)) #Append the current node to the fringe

                    #Sorting the fringe according to the heuristic function
                    fringe.sort(key=sort_acc_to_cost) # Sorts the fringe in ascending order accroding to the heuristic
  

    if flag == 0: # Returns '-1' if no path exists
        return (-1,"")                        


# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + solution[1])