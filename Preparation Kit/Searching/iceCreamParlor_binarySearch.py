#!/usr/bin/python3
#from itertools import combinations
#import numpy as np

def getValue(costs,a,b):
    for i in range(len(costs)):
        if costs[i] == a :
            for j in range(i+1,len(costs)):
                if costs[j] == b:
                    return (i,j)
        if costs[i] == b :
            for j in range(i+1,len(costs)):
                if costs[j] == a:
                    return (i,j)
    return None

def binarySearch(array,x):
    left = 0
    right = len(array) - 1;
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == x:
            return True
        elif x < array[mid]:
            right = mid - 1
        else : left = mid +1
    #print ("Not found")
    return False

def whatFlavors(costs,money):
    sorted_costs = sorted(costs)
    for i in range(len(sorted_costs)):
        a = sorted_costs[i]
        b = money - a
        index2 = binarySearch(sorted_costs[i+1:], b)
        if (index2):
            sol = getValue(costs,a,b)
            z = (min(sol[0]+1,sol[1]+1),) + (max(sol[0]+1,sol[1]+1),)
            #print(str(z[0])+" "+str(z[1]))
            return z
    return None

def main():
    t = int(input())
    stacks = []
    for t_itr in range(t):
        money = int(input())
        n = int(input())
        cost = list(map(int, input().rstrip().split()))
        stack = whatFlavors(cost, money)
        print("{} {}".format(stack[0], stack[1]))
        stacks.append(stack)

    return stacks

if __name__ == '__main__':
    main()
