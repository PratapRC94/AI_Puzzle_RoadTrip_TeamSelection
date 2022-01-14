#!/usr/local/bin/python3
# assign.py : Assign people to teams
#
# Code by: Pratap Roy Choudhury[prroyc@iu.edu] | Tanu Kansal[takansal@iu.edu] | Parth Ravindra Rao[partrao@iu.edu] 
#
# Based on skeleton code by D. Crandall and B551 Staff, September 2021
#

import sys

# reads data from input file and form a dictionary
def getDataFromReadFile( fileName ):
    with open( fileName, "r") as f:
        data = f.readlines()
    finalData = {}
    for i in data:
        finalData[ i.split()[0]] = [ i.split()[1] , i.split()[2]]
    return finalData

# calculates cost of the team formation
def calculateCost ( currentTeamMembers , initialData ):
    # initial cost every team must be having
    cost = 5
    currentTeamSize = len( currentTeamMembers )

    # Double-check if every person in team belongs to the initial Data
    for personName in currentTeamMembers: 
        if( personName not in initialData ):
            # return -1
            raise Exception("Internal Error")
        
        # getting details( requestTeamSize, requestedTeamMembers, notaRequiredMemebers) from provided inputs
        getPersonRequestedRecord = initialData[personName]
        requestedTeamMembers = getPersonRequestedRecord[0].split('-') 
        requestedTeamSize = len( requestedTeamMembers )
        notRequiredMembers = getPersonRequestedRecord[1].split(',')
        numberOfXXX = requestedTeamMembers.count('xxx') + requestedTeamMembers.count('zzz')

        # if team size is not given, as request, add 2 to the cost
        if( currentTeamSize != requestedTeamSize ):
            cost = cost + 2
        
        # check if member assigned was put in notRequired list by person
        for i in currentTeamMembers:
            if i != personName and i!='xxx' and i!='zzz': 
                if( i not in requestedTeamMembers):
                    if( i in notRequiredMembers ):
                        cost = cost + 10      
        # check if any team member requested by the person, not assigned
        for i in requestedTeamMembers:
            if( i != 'xxx' and i != 'zzz' ):
                if( i not in currentTeamMembers ):
                    cost = cost+3
    return cost

# to generate successors taking pool( available people ) and inpuitFile data as parameter
def generateSuccesors( pool, initialData , costMaintainance ):
    successors = []
    local = []

    # for every item/person in pool
    for i in range( len( pool )):
        # to make combinations
        for j in range( len(local)):
            # only add if size is less than 3, as maximum size can be 3 only
            if( len(local[j]) < 3 ):
                newTeam = local[j] + [ pool[i] ]
                newPool1 = list(pool)
                # making new pool and character string for cost evaluation
                current = ""
                for element in newTeam:
                    current= current+element
                    newPool1.remove( element)
                # formatting for storage
                current = sorted(current)
                current = "".join(current)
                # if cost for team already calculated use that , else, calculate cost
                if( current in costMaintainance):
                    cost = costMaintainance[current]
                else:
                    cost = calculateCost(  newTeam , initialData )               
                # appending/storing
                local.append(newTeam)
                successors.append( (( newTeam , newPool1 ), cost) )
                costMaintainance[ current ] = cost

        team = [ pool[i] ]
        # making new pool and character string for cost evaluation
        newPool = list(pool)
        newPool.remove( pool[i] )
        # formatting for storage
        current = pool[i]
        current = sorted(current)
        current = "".join(current)
        # if cost for team already calculated use that , else, calculate cost
        if( current in costMaintainance):
                cost = costMaintainance[current]
        else:
           cost = calculateCost(  team , initialData ) 
        # appending/storing
        local.append( team )
        successors.append( ((  team , newPool ), cost) )
        costMaintainance[ current ] = cost

    successors.sort(key=lambda x: x[1], reverse=True)
    return (successors, costMaintainance )


#solver function taking inputFile as parameter    
def solver( inputFile ):
    # converting input file data into dictionary( format : { "person" : [ requestedTeam, notWantedMembers ]})
    initialData = getDataFromReadFile( inputFile )
    # to keep the track of minimum Cost
    minCost = -1    
    # available people to form the team combinations
    pool = list(initialData.keys())
    # storage to maintain team cost
    costMaintainance= {}
    # fringe keeps track of the available combinations and perform DFS with essence of Pruning and A* Algorithm
    fringe = [ ( pool , 0 , [] )]

    # while fringe is not empty
    while( len( fringe )):
        # taking elements out of the fringe pop()
        ( currentPool, currentCost , currentPathTraced ) = fringe.pop()
        # generating successors for the same
        successorsArray , costMaintainance = generateSuccesors( currentPool , initialData, costMaintainance )
        # iterating through successors
        for successor in successorsArray:
            # taking elements out of the successor
            ((successorTeam, successorPool), successorCost) = successor
            # totalCost = successorCost + costTillNow on the path
            totalCostIncludingSuccessor = currentCost + successorCost
            # forming "person1"/"person1-person2"/"person1-person2-person3" format out of the team array
            currentTrace= ""
            lengthOfSuccessorTeam = len( successorTeam )
            for i in range(0, lengthOfSuccessorTeam-1 ):
                currentTrace = currentTrace+ successorTeam[i]+'-'
            currentTrace = currentTrace+successorTeam[ lengthOfSuccessorTeam-1 ]
            #path traced till now
            pathTracedIncludingSuccessor = currentPathTraced + [ currentTrace ]
            # if no one is available in pool, end that path
            if( len(successorPool) == 0 ):
                # if it is first combination evaluated or current cost is lower than previous one,
                # yield the result, and continue for better search
                if( minCost == -1 or totalCostIncludingSuccessor < minCost ):
                    minCost = totalCostIncludingSuccessor
                    yield({"assigned-groups": pathTracedIncludingSuccessor ,"total-cost" : totalCostIncludingSuccessor})
            # if totalCost is less then previous result cost, continue exploring on other paths
            if( (minCost == -1 or totalCostIncludingSuccessor <= minCost) and len(pool) ):
                fringe.append( ( successorPool , totalCostIncludingSuccessor , pathTracedIncludingSuccessor  ))


if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected an input filename"))

    for result in solver(sys.argv[1]):
        print("----- Latest solution:\n" + "\n".join(result["assigned-groups"]))
        print("\nAssignment cost: %d \n" % result["total-cost"])
    
