# Part 1: The 2021 Puzzle

Consider the 2021 puzzle, which is a lot like the 15-puzzle we talked about in class, but: (1) it has 25 tiles, so there are no empty spots on the board (2) instead of moving a single tile into an open space, a move in this puzzle consists of either (a) sliding an entire row of tiles left or right one space, with the left- or right-most tile "wrapping around" to the other side of the board, (b) sliding an entire column of tiles up or down one space, with the top- or bottom-most tile "wrapping around" to the other side of the board, (c) rotating the outer "ring" of tiles either clockwise or counterclockwise, or (d) rotating the inner ring either clockwise or counterclockwise.

The goal of the puzzle is to find a short sequence of moves that restores the canonical configuration given an initial board configuration. We've provided skeleton code to get you started. You can run the skeleton code on the command line:
```
python3 solver2021.py [input-board-filename]
```
where input-board-filename is a text file containing a board configuration (we have provided an example). You'll need to complete the function called solve(), which should return a list of valid moves. The moves should be encoded as strings in the following way:
* For sliding rows, R (right) or L (left), followed by the row number indicating the row to move left or right. The row numbers range from 1-5.
* For sliding columns, U (up) or D (down), followed by the column number indicating the column to move up or down. The column numbers range from 1-5.
* For rotations, I (inner) or O (outer), followed by whether the rotation is clockwise (c) or counterclock- wise (cc).

The initial code does not work correctly. Using this code as a starting point, implement a fast version, using A* search with a suitable heuristic function that guarantees finding a solution in as few moves as possible. Try to make your code as fast as possible even for dificult boards, although it is not necessarily possible to quickly solve all puzzles. For example, board1.txt can be solved in 11 moves. You will need to be creative with your heuristic function in order to find this solution in less than 15 minutes.

## Solution

The goal of this problem is to find the optimal moves to restore the canonical configuration of a given board configuration.


1. **What is the set of valid states space?** - *The set of valid state spaces are all the position that the tiles can take on the board.*
2. **The successor function?** - *The successor function will include all the possible moves the tiles can make, given a particular board. Given a particular board, the successor function will include all the boards once each column has been moved up or down which includes U1, U2, U3, U4, U5 and D1, D2, D3, D4, D5 moves, each row is moved right and left, and the outer and inner ring moves clockwise and anticlockwise.*
3. **The edge weights?** - *Here each move was equally weighted, which we have considered in the variable step.* 
4. **The goal state definition and the initial state?** - *The initial state can be any arrangement of 25 tiles between 1 to 25 in a 5x5 format. The goal state would be the tiles arranged in order from 1 to 25.*
5. **The heuristic function?** - *The heuristic function used here is a variation of misplaced tiles, where each move was adjusted using a constant value associated with each move. Once the number of misplaced tiles is calculated, if the move used to get there was a U, D, R or L move, we divided the value by 5 since there are 5 rows and columns, if it was a Outer ring move then we divide the value by 16 since there are 16 outer tiles, and if it is an inner ring move we divide it by 8 as there are 8 inner tiles. The heuristic is calculated in the **misplaced(state, move)** function.*

### Algorithm and Flow:

We implemented the algorithm using priority queues through **heapq** fringe which contained the total cost for the state, the board arrangement, the step number, and a string containing the moves made to reach that board.
   1. Once the board is read by the program, it is added to the fringe which we convert into a heap. 
   2. Looping through the fringe as long as it isn’t empty, we pop the fringe for the board with the least cost, and store the associated cost, board, steps and moves in different variables. The board is added to a visited list that stores all the states of the board already traversed in order to ensure that the same state isn’t visited twice.
   3. Next the current board is compared with the goal state in the **is_goal(state)** function returning the moves made until now, if it matches. 
   4. If it doesn’t match with the goal state, the loop iterates through the list of successors for the board using the **successors(state)** function, and checks if each successor is already in the visited list.
   5. If the board isn’t in the visited list, the heuristic is calculated using the **misplaced(state, move)** function and added to the number of steps taken so far, which is our total cost of the board. The moves taken to reach this state is updated and then these values are added into the fringe heap using the cost as the index for the heap.

*We would have to traverse about 24^7 states if we use a BFS instead of A*

### Challenges :

   * Prior to implementing misplaced tiles, we tried using a variation of ***Manhattan distance*** as a heuristic function using the manhattan_dist(state) function. We calculate the Manhattan distance between the current state and goal state, while also keeping in mind that the tiles wrap around each other, which means that a tile having to move from the end of a row to the beginning of the row needs only 1 move instead of 4. Similarly a tile move from the second last position to the first position can wrap around the row in 2 moves instead of 3 moves in the opposite direction.
   * While this heuristic gave us a quick solution, the solution was non-optimal for *board_0.5* giving us a solution of **9** instead of **7**. So we then used the ***misplaced(state, move)*** in order to get a better heuristic. The drawback of using this heuristic is that it took a lot of time, but it gave us an optimal solution for our boards. *board_0.5* gave an output of *7* moves in about ***22 minutes*** instead of the given **15 minutes time-out**.
   * We preferred to go with a heuristic that gives an optimal solution over a quicker solution with non-optimal moves and so our code currently uses ***misplaced(state, move)***. 


# Part 2: Road trip!

It's not too early to start planning a post-pandemic road trip! If you stop and think about it, finding the shortest driving route between two distant places - say, one on the east coast and one on the west coast of the U.S. - is extremely complicated. There are over 4 million miles of roads in the U.S. alone, and trying all possible paths between two places would be nearly impossible. So how can mapping software like Google Maps finnd routes nearly instantly? The answer is A* search!
We've prepared a dataset of major highway segments of the United States (and parts of southern Canada and northern Mexico), including highway names, distances, and speed limits; you can visualize this as a graph with nodes as towns and highway segments as edges. We've also prepared a dataset of cities and towns with corresponding latitude-longitude positions. Your job is to find good driving directions between pairs of cities given by the user.
The skeleton code can be run on the command line like this:
```
python3 ./route.py [start-city] [end-city] [cost-function]
```
where:
* **start-city** and **end-city** are the cities we need a route between.
* **cost-function** is one of:
	1. **segments** tries to find a route with the fewest number of road segments (i.e. edges of the graph).
	2. **distance** tries to find a route with the shortest total distance.
	3. **time** finds the fastest route, assuming one drives the speed limit.
	4. **delivery** finds the fastest route, in expectation, for a certain delivery driver. Whenever this driver drives on a road with a speed limit >= 50 mph, there is a 	chance that a package will fall out of their truck and be destroyed. They will have to drive to the end of that road, turn around, return to the start city to get a replacement, then drive all the way back to where they were (they won't make the same mistake the second time they drive on that road).
	
	Consequently, this mistake will add an extra *2 x (t_road +t_trip)* hours to their trip, where *t_trip* is the time it took to get from the start city to the beginning of the road, and *t_road* is the time it takes to drive the length of the road segment.
	
	For a road of length *l* miles, the probability *p* of this mistake happening is equal to tanh(*l/1000*) if the speed limit is >= 50 mph, and 0 otherwise. This means that, in expectation, it will take *t_road + p x 2 x (t_road + t_trip)* hours to drive on this road.

**For example**:
```
python3 ./route.py Bloomington,_Indiana Indianapolis,_Indiana segments

```

Our goal is to complete the *get route()* function given in the skeleton code, which returns the best route according to the specifed cost function, as well as the number of segments, number of miles, number of hours for a car driver, and expected number of hours for the delivery driver.

Like any real-world dataset, our road network has mistakes and inconsistencies; in the example above, for example, the third city visited is a highway intersection instead of the name of a town. Some of these "towns" will not have latitude-longitude coordinates in the cities dataset; you should design your code to still work
well in the face of these problems.

## Solution

The goal of this problem is to find the best route to travel from one city to another, following the optimal solution for a given cost function (segments/distance/time/delivery). 

A skeleton program was already given which is saved as route.py. We need to develop the search algorithm in order to find the solution.

1. **What is the set of valid state space?** - *The valid states are all the interconnected city combinations which are connected by a highway and distance,speed limit are available.*
2. **The successor function?** - *It identifies all the possible cities that can be reachable from the current city location via a highway. It returns the next city name,distance,speed limit,connecting highway,time required to travel and probability of travelling the route again due to overspeed.*
3. **The edge weights?** - *Here edge weights are the road distance for the distance cost function, time required to reach one city from current city for the time cost function, probability of doing the mistake of overspeeding for delivery cost function.*
4. **The goal state definition, and the initial state?** - *The goal state is the destination city. The initial state is the starting city provided by the user.*
5. **The heuristic function?** - *We have used the latitude and longitude of a city to find the heuristics. To get the efficient heuristic value, the best distance formula is haversine distance to find the distance between two geo-locations using their latitude and longitude. This Heuristic distance value is used according to the units of cost function, ie. if 'time' is the cost function, then we use heuristic/average speed of the dataset which gives heuristics in time unit.*

To run the program correctly and more efficiently, the **get_route(start, end, cost)** function has been modified in the skeleton code with the search algorithm, **successors(city,road_seg)** function has been defined to get the successor city list for the current city location, **get_heuristic(lat_1,long_1,lat_2,long_2)** function has been defined to calculate the heuristic value between two city locations.

### Algorithm

* **road_seg** - *road segment dataset of first city, second city, distance,speed,highway*
* **city_gps** - *dataset contains city, latitude, longitude*
* **fringe** - *A **heapq** FRINGE that contains the heuristic[**f(s')**], current city(**curr_city**),distance covered (**distance**) from the starting, trip time (**t_trip**) from the starting, total delivery time incurred (**delivery**) till now and the valid paths (**path**)which are visited till now - for the starting city location and subsequently for all the valid states from the successor function. 
It is a heap queue of lists where each list contains the information of next reachable cities. the root/parent of each list in the heapq is the cost function and the next best node is popped out based on the highest priority of the parent.*
* **visited_cities** - *a list to store all the visited moves to keep track of it so that it can be discarded in next move to make the heuristic consistent.*

### Algorithm : get_route(start, end, cost)

```
1. Initialise FRINGE with state s
2. While len(FRINGE)>=0, Repeat:
3   For every s' in SUCC(REMOVE(fringe),road_seg):
4.    get h(s') using s'.lat,s'.long and end.lat,end.long
5.	  if GOAL(s',end)?
6.		d <- distance + s'.length, t <- t_trip + s'.time, del_t <- delivery + (s'.time + prob*2*(t_trip+s'.time), p <- path + s'.(next_city,highway,length))
7.		return (len(p),d,t,del_t,p)
8.	  If s' not in visited_cities:
9.		f(s') <- g(s') + h(s'), where g(s') is the cost of best path found so far from s and h(s') is admissible heuristic function
10.		d <- distance + s'.length, t <- t_trip + s'.time, del_t <- delivery + (s'.time + prob*2*(t_trip+s'.time), p <- path + s'.(next_city,highway,length))
11.		INSERT((f(s'),s'.next_city,d,t,del_t,p), FRINGE)
12.     INSERT(s'.next_city,visited_cities)
13. If empty(FRINGE) then return False
```

### Algorithm : get_heuristic(lat_1,long_1,lat_2,long_2)

```
1. Initialise rad  = 0.621371*6371 (earth radius in miles)
2. del_lat = (lat_2 - lat_1) in radian
3. del_lon = (long_2 - long_1) in radian
4. hav <- sin^2(del_lat/2) + cos(lat_1)*cos(lat_2)*sin^2(del_lon/2)
5. hav_distance <- 2*rad*arcsin(sqrt(hav))
6. return hav_distance
```

### **Sample Output**

```
prroyc@silo:~/partrao-prroyc-takansal-a1$ python3 route.py Indianapolis,_Indiana Bloomington,_Indiana delivery      
Start in Indianapolis,_Indiana
   Then go to Jct_I-465_&_IN_37_S,_Indiana via IN_37 for 7 miles
   Then go to Martinsville,_Indiana via IN_37 for 25 miles
   Then go to Bloomington,_Indiana via IN_37 for 19 miles

          Total segments:    3
             Total miles:   51.000
             Total hours:    1.079
Total hours for delivery:    1.156
```

# Part 3: Choosing teams

In a certain Computer Science course, students are assigned to groups according to preferences that they specify. Each student is sent an electronic survey and asked to give answers to three questions:

   1. What is your IU email username?
   2. Please choose one of the options below and follow the instructions.
      (a) You would like to work alone. In this case, just enter your userid in the box and nothing else.
      (b) You would like to work in a group of 2 or 3 people and already have teammates in mind. In
      this case, enter all of your userids (including your own!) in the box below, in a format like
      userid1-userid2 for a team of 2, or userid1-userid2-userid3 for a team of 3.
      (c) You would like to work in a group of 2 or 3 people but do not have any particular teammates in
      mind. In this case, please enter your user ID followed by one \zzz" per missing teammate (e.g.
      djcran-zzz where djcran is your user ID to request a team of 2, or djcran-zzz-zzz for a team of 3).
      (d) You would like to work in a group of 3 people and have some teammates in mind but not all.
      Enter all of your ids, with zzz's to mark missing teammates (e.g. if I only have one teammate
      (vkvats) in mind so far, I'd enter djcran-vkvats-zzz).
   3. If there are any people you DO NOT want to work with, please enter their userids here (separated by commas, e.g. userid1,userid2,userid3).

Unfortunately | and as we already discovered while assigning teams for Assignment 1 -- the student preferences may not be compatible with each other: student A may request working with student B, but B may request not to work with A, for example. Students are going to complain, so the course staff decides to minimize their own work. They estimate that:

   * It will take 5 minutes to grade each assignment, so total grading time is 5 times the number of teams.
   * Each student who requested a specific group size and was assigned to a different group size will send a complaint email to an instructor, and it will take the instructor 2 minutes to read this email.
   * If a student is not assigned to someone they requested, there is a 5% probability that the two students will still share code, and if this happens it will take 60 minutes for the instructor to walk through the Academic Integrity Policy with them. If a student requested to work with multiple people, then this will happen independently for each person they were not assigned to. If both students requested each other, there will be two meetings.
   * Each student who is assigned to someone they requested not to work with (in question 3 above) complains to the Dean, who meets with the instructor for 10 minutes. If a student is assigned to a group with multiple people they did not want to work with, a separate meeting will be needed for each.

The total time spent by the course staff is equal to the sum of these four components. You can assume that each student fills out the survey exactly once, and fills it out according to the instructions. Your goal is to write a program to find an assignment of students to teams that minimizes the total amount of work the staff needs to do, subject to the constraint that no team may have more than 3 students. Your program should take as input a text file that contains each student’s response to these questions on a single line, separated by spaces. For example, a sample file might look like:

```
   **djcran djcran-vkvats-nthakurd sahmaini
   sahmaini sahmaini _
   sulagaop sulagaop-xxx-xxx _
   fanjun fanjun-xxx nthakurd
   nthakurd nthakurd djcran,fanjum
   vkvats vkvats-sahmaini _**
```
where the underscore character *(_)* indicates an empty value.

We have provided skeleton code to get you started, which can be run like: 
```
python3 ./assign.py [input-file]
```
The job is to complete the **solver()** function. The function should return the final groups (each named according to the students in the group, separated by hyphens), and the total cost (time spent by instructors in minutes). For example, one assignment for the above file could be:
   **["djcran-vkvats-nthakurd", "sahmaini", "sulagaop-fanjun"]**
which has a cost of 34, computed by the sum of: 
   1. There are three groups' assignments to grade (3x5 = 15 minutes) 
   2. Three people (sulagaop, nthakurd, and vkvats) didn't get the requested number of teammates (3x2 = 6 minutes) 
   3. One person (nthakurd) had to work with someone they requested not to work with (djcran) (10 minutes) 
   4. One person (vkvats) didn't get to work with a person they requested (sahmaini) (0:05 x 60 = 3 minutes)

## Solution

### Strategy:

   * Using a stack as my fringe data structure.
   * Fringe is storing all the combinations, keeping cost in track.
   * Generate a list(pool), containing all people who are yet to be assigned to a team
   * Generate poosible combination of them in a team of maximum 3
   * Calculate cost for each combination( Also, keep storage of them to avoid re-computations, as there is very high probability of repetition)
   * Generate successors for each combination and apply Depth First Algorithm, with the essesnce of A* and Pruning algorithm.
   * When my pool becomes empty, yield the path traced till current situation and cost for the combinations.

### Algorithm:

```
   1. Parse the input file, and form a dictionary  containing { person : [ teamRequestedByPerson, teamNotWantToWorkWith ]}
   2. Get Keys from the dictionary and put in a list
   3. Form a fringe( list data structure), and put a root value
      i.e. fringe = [ ( pool , 0 , [] )]
      which is quivalent to, fringe = [ pool, cost , pathTraced ]
      where, 
      pool = list of all person which are not assigned a team yet
      cost = cost till now( cost of combination formed till now, for the particular path )
      pathTraced = contain all the combinations of the path we are following
   4. While( len(fringe )):
      1. Pop the last element from the fringe
      2. Generate all the successors by following steps:
               1. Iterate through all the person in pool :
                     1. Generate all the combinations of 1 , 2, 3 and find cost for each combination.
                           Check if cost for the combination is already stored. If not, to calculate the cost, do the following steps:
                              1. Take initial cost as 5, as it is grading cost for every combination.
                              2. Iterate through every person in the combination:
                                       * check if the combination size is different from what they requested, add 2 to cost
                                       * 10 for such member, person put in notWanted list but anyway assigned in the combination.
                                       * 3 for each such member the person requested to form a team, but not assigned/present in the combination.
                                       * add all to calculate the total cost of the combination
                     2. Maintain a dictionary containing cost for each cobination, as to avoid recomputation in future. There is very high probablity of repetition.
                     3. Append all the successors in a list
      3. Iterate through all the successors:
         1. calculate the costTillNow, including cost of the successor
         2. Store pathTracedTillNow, including successor combination
         3. Check if pool returned is empty:
               If yes,
                  1. if costTillNow < minCost( where, minCost contains the cost of lowest succesful team formation till now )
                     If yes, yeild the result and continue for better solutions.
               Else,
                  check If costTillNow is exceeding the cost of previous solution, prune it
                  If not, append it to fringe.
      4. return
```

### **Sample Output**

```
prataprc94@Prataps-MacBook-Pro part3 % python3 assign.py test1.txt
----- Latest solution:
nthakurd
sahmaini
fanjun
djcran-sulagaop-vkvats

Assignment cost: 30 

----- Latest solution:
nthakurd
sahmaini-vkvats
djcran-sulagaop-fanjun

Assignment cost: 25 

----- Latest solution:
sahmaini-sulagaop-nthakurd
djcran-fanjun-vkvats

Assignment cost: 24 
```
