#!/usr/bin/python3

import math
import os
import random
import numpy as np
import re
import sys



# Complete the checkMagazine function below.

def clear_steps(s):
    for i in range (k):
        for j in range (m):

            if ( (SM[i][j]) > s):
                SM[i][j] = -1


def where_to_move (pos):
    ## return '0-3' array of posible next_pos need to know limits, board and steps
    r=[]

    if pos is not None:

        if (pos[0]+1 < k) and (SM[(pos[0]+1)][pos[1]] < 0) :
            next_pos=[pos[0]+1,pos[1]]
            r.append(next_pos)
        if (pos[0] > 0) and (SM[(pos[0]-1)][pos[1]] < 0) :
            next_pos=[pos[0]-1,pos[1]]
            r.append(next_pos)
        #Down
        if (pos[1]+1 < m) and (SM[pos[0]][pos[1]+1] < 0)  :
            next_pos=[pos[0],pos[1]+1]
            r.append(next_pos)
        if  pos[1] >0 and (SM[pos[0]][(pos[1]-1)] < 0) :
            next_pos=[pos[0],pos[1]-1]
            r.append(next_pos)

    return r

def pushStep(pos,step):
    DP_pool.append([pos,step])
    #print(DP_pool)

def pull_not_empty():
    if DP_pool == []:#Found a way
        r = False
    else: r = True
    return r

def popStep():
    if DP_pool != []:
        r = DP_pool.pop(len(DP_pool)-1)
    else: r = None
    #print(DP_pool)
    return r


def move_to (pos,step):

    global tk
    global step_old
    global pos_old

    SM_old = []
    SM[pos[0]][pos[1]]=step
    #print (SM)
    #print ("Current step :", step)

    step = step+1

    if step == (m*k) and pos == [0,m-1] :
        tk=tk+1
        #pos=[0,0]
        #print ("Way Founds :", tk)
        #clear_steps(step)
        #return


    #print ("Where to move :", where_to_move(pos))
    moves = where_to_move(pos)
    for i in moves :
        #SM_old = SM
        pushStep(pos,step-1)
        move_to(i,step)
        [pos, step] = popStep()
        #print ("Step poped: ", step)
        clear_steps(step)
        step =step +1




    return



def tCount(m,i):
    global DP_pool
    global SM
    DP_pool = []
    SM = []    #magazine = input().rstrip().split()
    global tk#Step Matrix
    global k
    global step
    SM = np.ones((i,m),dtype=int)

    #declare matrixdef where_to_move (pos,route_taken):
    #print (SM)

    k = i
    tk = 0

    SM[0][0]=0
    #print (SM[0][0])
    step = 0
    clear_steps(step)

    pos = move_to([0,0],step)

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
    print (result)
