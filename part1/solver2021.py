#!/usr/local/bin/python3
# solver2021.py : 2021 Sliding tile puzzle solver
#
# Code by: Pratap Roy Choudhury[prroyc@iu.edu] | Tanu Kansal[takansal@iu.edu] | Parth Ravindra Rao[partrao@iu.edu] 
#
# Based on skeleton code by D. Crandall & B551 Staff, September 2021
#

import sys
import heapq as hq
import time

ROWS=5
COLS=5

def printable_board(board):
    return [ ('%3d ')*COLS  % board[j:(j+COLS)] for j in range(0, ROWS*COLS, COLS) ]

# Modified Manhattan Heuristic
def manhattan_dist(state, move):
    score = 0
    for pos in range(len(state)):
        hor_shift = abs((state[pos]-1)%5 - pos%5) 
        if hor_shift == 3:
            hor_shift = 2
        elif hor_shift == 4:
            hor_shift = 1

        vert_shift = abs((state[pos]-1)//5 - pos//5)
        if vert_shift == 3:
            vert_shift = 2
        elif vert_shift == 4:
            vert_shift = 1
        score += vert_shift + hor_shift
    return score

# Misplaced Tiles Heuristic
def misplaced(state, move):
    if move == '':
        adjust = 1
    elif move[0] in ["U","D", "R","L"]:
        adjust = 5
    elif move[0] == "O":
        adjust = 16
    elif move[0] == "I":
        adjust = 8

    dist = 0
    for i in range(ROWS*COLS):
        if state[i] != i+1:
            dist+=1

    return dist/adjust

# return a list of possible successor states
def successors(state):
    # Return all the possible states from a particular current state (set of tuples), with moves
    succ_states = []

    # Move RIGHT for each row
    for row in range(ROWS):
        row+=1
        new_state = list(state[:])
        temp = new_state[(row*COLS)-1]
        for element in range((row*COLS)-1,(row*COLS)-6,-1):
            new_state[element] = new_state[element - 1]
        new_state[(row*COLS)-5] = temp
        move = "R"+str(row)
        succ_states.append((tuple(new_state), move))

    # Move LEFT for each row
    for row in range(ROWS):
        row+=1
        new_state = list(state[:])
        temp = new_state[(row*COLS) - 5]
        for element in range((row*COLS) - 4,(row*COLS)):
            new_state[element - 1] = new_state[element]
        new_state[(row*COLS)-1] = temp
        move = "L"+str(row)
        succ_states.append((tuple(new_state), move))

    # Move UP for each column
    for col in range(COLS):
        new_state = list(state[:])
        temp = new_state[col]
        for element in range(col+5, ROWS*COLS, 5):
            new_state[element - 5] = new_state[element] 
        new_state[(ROWS*COLS)-(5-col)] = temp
        move = "U"+str(col+1)
        succ_states.append((tuple(new_state), move))

    # Move DOWN for each column
    for col in range(COLS):
        new_state = list(state[:])
        temp = new_state[ROWS*COLS - (5-col)]
        for element in range(ROWS*COLS - (5-col), -1, -5):
            new_state[element] = new_state[element - 5]
        new_state[col] = temp
        move = "D"+str(col+1)
        succ_states.append((tuple(new_state), move))

    # For circular movement
    outer_indices = [0,1,2,3,4,9,14,19,24,23,22,21,20,15,10,5,0]
    inner_indices = [6,7,8,13,18,17,16,11,6]

    # Move OUTER CLOCKWISE
    new_state = list(state[:])
    temp = new_state[0]
    for pos in range(len(outer_indices)-2,-1, -1):
        new_state[outer_indices[pos+1]] = new_state[outer_indices[pos]]
    new_state[1] = temp
    move = "Oc"
    succ_states.append((tuple(new_state), move))
    
    # Move OUTER COUNTER CLOCKWISE
    new_state = list(state[:])
    temp = new_state[0]
    for pos in range(len(outer_indices)-2):
        new_state[outer_indices[pos]] = new_state[outer_indices[pos+1]]
    new_state[outer_indices[-2]] = temp
    move = "Occ"
    succ_states.append((tuple(new_state), move))

    # Move INNER CLOCKWISE
    new_state = list(state[:])
    temp = new_state[inner_indices[0]]
    for pos in range(len(inner_indices)-2,-1, -1):
        new_state[inner_indices[pos+1]] = new_state[inner_indices[pos]]
    new_state[inner_indices[1]] = temp
    move = "Ic"
    succ_states.append((tuple(new_state), move))

    # Move INNER COUNTER CLOCKWISE
    new_state = list(state[:])
    temp = new_state[inner_indices[0]]
    for pos in range(len(inner_indices)-2):
        new_state[inner_indices[pos]] = new_state[inner_indices[pos+1]]
    new_state[inner_indices[-2]] = temp
    move = "Icc"
    succ_states.append((tuple(new_state), move))

    return succ_states

# check if we've reached the goal
def is_goal(state):
    goal = False
    for num in state:
        if int(num) == state.index(num) + 1:
            goal = True
        else:
            goal = False
            break
    return goal

def solve(initial_board):
    start = time.time()
    """
    1. This function should return the solution as instructed in assignment, consisting of a list of moves like ["R2","D2","U1"].
    2. Do not add any extra parameters to the solve() function, or it will break our grading and testing code.
       For testing we will call this function with single argument(initial_board) and it should return 
       the solution.
    3. Please do not use any global variables, as it may cause the testing code to fail.
    4. You can assume that all test cases will be solvable.
    5. The current code just returns a dummy solution.
    """
    visited = []
    fringe = []

    # Add initial_board to fringe
    fringe.append([misplaced(initial_board, ''), initial_board, 0, ''])
    hq.heapify(fringe)

    while len(fringe)>0:
        # Get the next best board from fringe
        (cost, current_board, step, move_list) = hq.heappop(fringe)
        
        if current_board not in visited:
            visited.append(current_board)

        if is_goal(current_board):

            # Handling case when the original board is the goal state
            try:
                if move_list.strip().split(' ').remove('') == None:
                    return []
            except:
                return move_list.strip().split(' ')

        states = successors(current_board)

        for state, move in states:

            if state not in visited:
                distance = misplaced(state, move)
                cost = distance + step + 1

                hq.heappush(fringe, (cost, state, step+1, move_list+" "+move))

    if len(fringe)==0:
        return []

# Please don't modify anything below this line
#
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a board filename"))

    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [ int(i) for i in line.split() ]

    if len(start_state) != ROWS*COLS:
        raise(Exception("Error: couldn't parse start state file"))

    print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))

    print("Solving...")
    route = solve(tuple(start_state))

    print("Solution found in " + str(len(route)) + " moves:" + "\n" + " ".join(route))
