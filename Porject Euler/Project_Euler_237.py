#!/usr/bin/python3

import math
import os
import random
import numpy
import re
import sys

# Complete the checkMagazine function below.



def move_to (next_pos,step):
    print ("moving to next pos:", next_pos)
    SM[next_pos[0]][next_pos[1]] = step
    return next_pos

def where_to_move (pos,route_taken):
    ## return '0-3' array of posible next_pos need to know limits, board and steps
    r=[]
    prev_step[0] = prev_step[1]
    prev_step[1] = pos
    # route taken can have size
    #print (pos, route_taken)
    # 4 possible directions
    #rightSM[pos[0]][pos[1]+1] == 0
    if pos is not None:

        # not working eliminate diagonal move


        if ([pos[0]+1,pos[1]] != route_taken) and (pos[0]+1 < k) and (SM[(pos[0]+1)][pos[1]] < 0) and ([pos[0]+1,pos[1]] != prev_step[0]) and ([pos[0]+1,pos[1]] != prev_step[1]):
            next_pos=[pos[0]+1,pos[1]]
            r.append(next_pos)
        if ([pos[0]-1,pos[1]] != route_taken) and (pos[0] > 0) and (SM[(pos[0]-1)][pos[1]] < 0) and ([pos[0]+1,pos[1]] != prev_step[0])and ([pos[0]+1,pos[1]] != prev_step[1]):
            next_pos=[pos[0]-1,pos[1]]
            r.append(next_pos)
        #Down
        if ([pos[0],pos[1]+1] != route_taken) and (pos[1]+1 < m) and (SM[pos[0]][pos[1]+1] < 0) and ([pos[0]+1,pos[1]] != prev_step[0])and ([pos[0]+1,pos[1]] != prev_step[1]) :
            next_pos=[pos[0],pos[1]+1]
            r.append(next_pos)
        if ([pos[0],pos[1]-1] != route_taken) and pos[1] >0 and (SM[pos[0]][(pos[1]-1)] < 0) and ([pos[0]+1,pos[1]] != prev_step[0])and ([pos[0]+1,pos[1]] != prev_step[1]):
            next_pos=[pos[0],pos[1]-1]
            r.append(next_pos)



    return r

def follow_route(pos,route_taken,s):
    global step#Found a way

    step = s


    while (where_to_move(pos,route_taken) != []) and (step< m*k) and (pos!= (k-1,m-1)):
        #print(where_to_move(pos,route_taken))
        print("I can move to" , where_to_move(pos,route_taken))
        #if  step==5 :
        #    break
        if len(where_to_move(pos,route_taken)) > 1:

            next_pos= where_to_move(pos,route_taken)[0]

            push_to_pool(pos,next_pos,step)
            step = step +1
            pos = move_to(next_pos,step)

        else:
            next_pos= where_to_move(pos,route_taken)[0]
            step = step +1
            pos = move_to(next_pos,step)

        print("I can move to " , where_to_move(pos,route_taken))
        print (SM)
    return step

def clear_steps(step):
    for i in range (k):
        for j in range (m):
            if (SM[i][j] > step):
                SM[i][j] = -1

def push_to_pool(pos,next_pos,step):
    DP_pool.append([pos,next_pos,step])
    print(DP_pool)

def pull_not_empty():
    if DP_pool == []:#Found a way
        r = False
    else: r = True
    return r

def pull_from_pool():
    if DP_pool != []:
        r = DP_pool.pop(len(DP_pool)-1)
    else: r = None
    print(DP_pool)
    return r

def tCount(m,i):
    global k
    global SM #Step Matrix
    global DP_pool#Found a waySM[pos[0]:][pos[1]:] = 0
    global prev_step

    DP_pool = []
    SM = numpy.ones(shape=(i,m))#declare matrixdef where_to_move (pos,route_taken):
    print (m,i)

    k = i
    tk = 0
    pos = [0,0]
    SM[0][0]=0
    route = [1,0]
    prev_step = [[0,0],[0,0]]
    steps = 0
    clear_steps(steps)
    push_to_pool(pos,route,steps)

    steps = 1
    pos = move_to(route,steps)

    #route = []#Found a way
    while pull_not_empty() and (steps < (m*k)):
        print (pos, route, steps, k)

        steps = follow_route(pos,route,steps)
        #if tk > 0 and steps< 8 : break
        print ("steps given ",steps)
        #prev_step[0] = prev_step[1]=[0,0]

        if steps == (m*k-1):
            tk = tk+1
            #Found a way
            print ("Found a way Tk: ",tk)


        if pull_not_empty(): #Go back to last decision point

            print ("Paso previo: ", prev_step )
            [pos,route,steps] =  pull_from_pool()
            prev_step[0] = prev_step[1]
            prev_step[1] = route

            print ("New DP pulled", pos, route, steps)
            print (SM)
            ## Clear any element > steps
            clear_steps(steps)
            #SM[route[0]][route[1]]=0
            print (SM)


            print("I can move to " , where_to_move(pos,route))
            #if (where_to_move(pos,route) != []):
                #route = where_to_move(pos,route)[0]

            #Found a way steps)
            #print (pull_not_empty(),steps,(m*k))

            # Reste tBoard
    return tk


def sCount(m,n):
    r=0
    for i in range(n): #should be 1 to#Found a way
        r+=tCount(m,i)
    return r

if __name__ == '__main__':
    #print ("what's this?")
    m = int(input())
    n = int(input())

    #magazine = input().rstrip().split()
    result = tCount(m,n)
    print ("Ways Found: ",result)
