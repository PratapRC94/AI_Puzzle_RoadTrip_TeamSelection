#!/usr/local/bin/python3
# route.py : Road Trip - Find routes through maps
#
# Code by: Pratap Roy Choudhury[prroyc@iu.edu] | Tanu Kansal[takansal@iu.edu] | Parth Ravindra Rao[partrao@iu.edu] 
#
# Based on skeleton code by V. Mathur and D. Crandall, January 2021
#


# !/usr/bin/env python3
import sys
import pandas as pd
import numpy as np
import math
import heapq

'''
road_seg = pd.read_csv("road-segments.txt",
                      names = ['city_1','city_2','length','speed','highway'],
                      usecols = [x for x in range(0,5)],
                      dtype = {'city':str,'city_2':str,'length':int,'speed':int,'highway':str},
                      sep = ' ',
                      header = None)
road_seg['time'] = round(road_seg.length/road_seg.speed,5)
road_seg['prob_overspeed'] = 0
road_seg.loc[road_seg['speed']>=50,'prob_overspeed'] = np.tanh(road_seg.loc[road_seg['speed']>=50]['length']/1000)

city_gps = pd.read_csv("city-gps.txt",
                      names = ['city','lat','long'],
                      usecols = [x for x in range(0,3)],
                      dtype = {'city':str,'lat':float,'long':float},
                      sep = ' ',
                      header = None)
'''
#successor function to get the list of successor city and details for a given city location
def successors(city,road_seg):

    next_city_details = []
    for i in range(road_seg.shape[0]):
        if road_seg.city_1[i] == city:
            next_city_details.append([road_seg.city_2[i],road_seg.length[i],road_seg.speed[i],road_seg.highway[i],road_seg.time[i],road_seg.prob_overspeed[i]])
        elif road_seg.city_2[i] == city:
            next_city_details.append([road_seg.city_1[i],road_seg.length[i],road_seg.speed[i],road_seg.highway[i],road_seg.time[i],road_seg.prob_overspeed[i]])
    return next_city_details

############################################################ Reference Code Start #############################################################################################
#https://stackoverflow.com/questions/36873187/heuristic-for-an-a-path-finding-gps?rq=1
#function to calculate the heuristic distance between two points using haversine formula
def get_heuristic(lat_1,long_1,lat_2,long_2):
    rad = 0.621371*6371 #in miles
    dLat = (lat_2-lat_1)*(math.pi/180)
    dLon = (long_2-long_1)*(math.pi/180)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(lat_1*(math.pi/180)) * math.cos(lat_2*(math.pi/180)) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = rad * c; 
    return d
############################################################ Reference Code End #############################################################################################


def get_route(start, end, cost):
    
    """
    Find shortest driving route between start city and end city
    based on a cost function.

    1. Your function should return a dictionary having the following keys:
        -"route-taken" : a list of pairs of the form (next-stop, segment-info), where
           next-stop is a string giving the next stop in the route, and segment-info is a free-form
           string containing information about the segment that will be displayed to the user.
           (segment-info is not inspected by the automatic testing program).
        -"total-segments": an integer indicating number of segments in the route-taken
        -"total-miles": a float indicating total number of miles in the route-taken
        -"total-hours": a float indicating total amount of time in the route-taken
        -"total-delivery-hours": a float indicating the expected (average) time 
                                   it will take a delivery driver who may need to return to get a new package
    2. Do not add any extra parameters to the get_route() function, or it will break our grading and testing code.
    3. Please do not use any global variables, as it may cause the testing code to fail.
    4. You can assume that all test cases will be solvable.
    5. The current code just returns a dummy solution.
    """

    #read the road segment dataset
    road_seg = pd.read_csv("road-segments.txt",
                      names = ['city_1','city_2','length','speed','highway'],
                      usecols = [x for x in range(0,5)],
                      dtype = {'city':str,'city_2':str,'length':int,'speed':int,'highway':str},
                      sep = ' ',
                      header = None)
    #calculate time from the available segment distance and speed
    road_seg['time'] = round(road_seg.length/road_seg.speed,5)
    #calculate the probability of overspeeding mistake for each segment, if not then 0
    road_seg['prob_overspeed'] = 0
    road_seg.loc[road_seg['speed']>=50,'prob_overspeed'] = np.tanh(road_seg.loc[road_seg['speed']>=50]['length']/1000)

    #read the city_gps dataset
    city_gps = pd.read_csv("city-gps.txt",
                          names = ['city','lat','long'],
                          usecols = [x for x in range(0,3)],
                          dtype = {'city':str,'lat':float,'long':float},
                          sep = ' ',
                          header = None)

    fringe = []
    visited_cities = []
    visited_cities.append(start)

    #for the given end city argument, store the latitude and longitude for heuristic distance calculation from the successor cities
    if end in city_gps.city.unique():
        lat2 = city_gps[city_gps.city == end]['lat'].iloc[0]
        long2 = city_gps[city_gps.city == end]['long'].iloc[0]

    #road trip information for cost function 'segments'
    if cost == 'segments':
        heapq.heappush(fringe,(0,start,0,0,0,[])) #heuristic cost segment, current city, distance,time, extra delivery time, path
        while len(fringe) != 0:
            #heapq pops the highest priority element based on the cost function set as root
            (segment, curr_city, distance, t_trip, delivery, path) = heapq.heappop(fringe)
            for (next_city,length,speed,highway,t_road,prob) in successors(curr_city,road_seg):
                #get the latitude and longitude of the current city in successor state and find the heuristic distance from the end city
                try:
                    lat1 = city_gps[city_gps.city == next_city]['lat'].iloc[0]
                    long1 = city_gps[city_gps.city == next_city]['long'].iloc[0]
                    h =  get_heuristic(lat1,long1,lat2,long2)
                except:
                    h = 0

                #check if goal state
                if next_city == end:
        
                    #d = distance + length
                    #t = t_trip + t_road
                    #del_time = round(delivery + (t_road + prob*2*(t_trip+t_road)),4)
                    path.append((next_city,highway+" for "+str(length)+" miles"))

                    return {"total-segments" : len(path), 
                            "total-miles" : float(distance + length), 
                            "total-hours" : t_trip + t_road, 
                            "total-delivery-hours" : round(delivery + (t_road + prob*2*(t_trip+t_road)),4), 
                            "route-taken" : path}

                elif next_city not in visited_cities:
                    #print(next_city)
                    #cost_seg = len(path) + 1
                    #cost_seg = len(path) + h/(road_seg.length.mean()) #heuristic
                    cost_seg = len(path) + h/(road_seg.length.max()) #heuristic
                    del_time = round(delivery + t_road + prob*2*(t_trip+t_road),4)
                    movement = (next_city,highway+" for "+str(length)+" miles")
                    #path.append([next_city,length,highway,t_road,del_time])
                    heapq.heappush(fringe,(cost_seg,next_city,distance+length,t_trip+t_road,del_time,path+[movement]))
                    #store the current city in visited city list to keep a track and discard traveling the same next time
                    visited_cities.append(next_city)

    #road trip information for cost function 'distance'
    if cost == 'distance':
        heapq.heappush(fringe,(0,start,0,0,0,[])) #heuristic cost distance, current city, distance,time, extra delivery time, path
        while len(fringe) != 0:
            #heapq pops the highest priority element based on the cost function set as root
            (heuristic, curr_city, distance, t_trip, delivery, path) = heapq.heappop(fringe)
            for (next_city,length,speed,highway,t_road,prob) in successors(curr_city,road_seg):
                #get the latitude and longitude of the current city in successor state and find the heuristic distance from the end city
                try:
                    lat1 = city_gps[city_gps.city == next_city]['lat'].iloc[0]
                    long1 = city_gps[city_gps.city == next_city]['long'].iloc[0]
                    h =  get_heuristic(lat1,long1,lat2,long2)
                except:
                    h = 0
                #check if goal state
                if next_city == end:
                    path.append((next_city,highway+" for "+str(length)+" miles"))
                    return {"total-segments" : len(path), 
                            "total-miles" : float(distance + length), 
                            "total-hours" : t_trip + t_road, 
                            "total-delivery-hours" : round(delivery + (t_road + prob*2*(t_trip+t_road)),4), 
                            "route-taken" : path}

                elif next_city not in visited_cities:
                    cost_dist = distance + h
                    del_time = round(delivery + t_road + prob*2*(t_trip+t_road),4)
                    movement = (next_city,highway+" for "+str(length)+" miles")
                    heapq.heappush(fringe,(cost_dist,next_city,distance+length,t_trip+t_road,del_time,path+[movement]))
                    #store the current city in visited city list to keep a track and discard traveling the same next time
                    visited_cities.append(next_city)

    #road trip information for cost function 'time'
    if cost == 'time':
        heapq.heappush(fringe,(0,start,0,0,0,[])) #heuristic cost time, current city, distance,time, extra delivery time, path
        while len(fringe) != 0:
            #heapq pops the highest priority element based on the cost function set as root
            (heuristic, curr_city, distance, t_trip, delivery, path) = heapq.heappop(fringe)
            for (next_city,length,speed,highway,t_road,prob) in successors(curr_city,road_seg):
                #get the latitude and longitude of the current city in successor state and find the heuristic distance from the end city
                try:
                    lat1 = city_gps[city_gps.city == next_city]['lat'].iloc[0]
                    long1 = city_gps[city_gps.city == next_city]['long'].iloc[0]
                    h =  get_heuristic(lat1,long1,lat2,long2)
                except:
                    h = 0
                #check if goal state
                if next_city == end:
                    path.append((next_city,highway+" for "+str(length)+" miles"))
                    return {"total-segments" : len(path), 
                            "total-miles" : float(distance + length), 
                            "total-hours" : t_trip + t_road, 
                            "total-delivery-hours" : round(delivery + (t_road + prob*2*(t_trip+t_road)),4), 
                            "route-taken" : path}

                elif next_city not in visited_cities:
                    #cost_time = t_trip + h/(road_seg.speed.mean()) #heuristic
                    cost_time = t_trip + h/(road_seg.speed.max()) #heuristic
                    del_time = round(delivery + t_road + prob*2*(t_trip+t_road),4)
                    movement = (next_city,highway+" for "+str(length)+" miles")
                    heapq.heappush(fringe,(cost_time,next_city,distance+length,t_trip+t_road,del_time,path+[movement]))
                    #store the current city in visited city list to keep a track and discard traveling the same next time
                    visited_cities.append(next_city)

    #road trip information for cost function 'delivery'
    if cost == 'delivery':
        heapq.heappush(fringe,(0,start,0,0,0,[])) #heuristic cost delivery time, current city, distance,time, extra delivery time, path
        while len(fringe) != 0:
            #heapq pops the highest priority element based on the cost function set as root
            (heuristic, curr_city, distance, t_trip, delivery, path) = heapq.heappop(fringe)
            for (next_city,length,speed,highway,t_road,prob) in successors(curr_city,road_seg):
                #get the latitude and longitude of the current city in successor state and find the heuristic distance from the end city
                try:
                    lat1 = city_gps[city_gps.city == next_city]['lat'].iloc[0]
                    long1 = city_gps[city_gps.city == next_city]['long'].iloc[0]
                    h =  get_heuristic(lat1,long1,lat2,long2)
                except:
                    h = 0
                #check if goal state
                if next_city == end:
                    path.append((next_city,highway+" for "+str(length)+" miles"))
                    return {"total-segments" : len(path), 
                            "total-miles" : float(distance + length), 
                            "total-hours" : t_trip + t_road, 
                            "total-delivery-hours" : round(delivery + (t_road + prob*2*(t_trip+t_road)),4), 
                            "route-taken" : path}

                elif next_city not in visited_cities:
                    #cost_del_time = delivery + prob*(h/(road_seg.speed.mean())) #heuristic
                    cost_del_time = delivery + prob*(h/(road_seg.speed.max())) #heuristic
                    del_time = round(delivery + t_road + prob*2*(t_trip+t_road),4)
                    movement = (next_city,highway+" for "+str(length)+" miles")
                    heapq.heappush(fringe,(cost_del_time,next_city,distance+length,t_trip+t_road,del_time,path+[movement]))
                    #store the current city in visited city list to keep a track and discard traveling the same next time
                    visited_cities.append(next_city)

    
# Please don't modify anything below this line
#
if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise(Exception("Error: expected 3 arguments"))

    (_, start_city, end_city, cost_function) = sys.argv
    if cost_function not in ("segments", "distance", "time", "delivery"):
        raise(Exception("Error: invalid cost function"))

    result = get_route(start_city, end_city, cost_function)

    # Pretty print the route
    print("Start in %s" % start_city)
    for step in result["route-taken"]:
        print("   Then go to %s via %s" % step)

    print("\n          Total segments: %4d" % result["total-segments"])
    print("             Total miles: %8.3f" % result["total-miles"])
    print("             Total hours: %8.3f" % result["total-hours"])
    print("Total hours for delivery: %8.3f" % result["total-delivery-hours"])


