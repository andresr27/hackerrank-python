#!/usr/bin/python3
#from itertools import combinations
#import numpy as np
def build_dict_table(keys,values):
    hash_map = {}
    for key,value in zip(keys,values):
        hash_key = key
        if key in hash_map:
            values = [hash_map[hash_key],value]
            hash_map[hash_key] = values
        else:
            hash_map[hash_key] = value
    return hash_map # Need to be sorted

def get_value(hash_map, key):
    if key in hash_map:
        values = hash_map[key]
        return values
    else:
        return None

def binarySearch(array,x):
    #print("BS Array: " + str(array))
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
    #hash_table = {k:v for k, v in zip(indexes, costs)}
    indexes = range(len(costs))
    table = build_dict_table(costs,indexes)
    #return "1 2"
    sorted_costs = sorted(costs)
    #flavors = combinations(costs,2)
    m = money // 2
    print ("Money: " + str(money))
    print ("Flavors: " + str(len(costs)))
    for a in costs:
        b = money - a
        f1 = get_value(table, a)
        f2 = get_value(table, b)
        if (f1 is not None) and (f2 is not None):
            # print ("Flavor 1: " + str(f1))
            # print ("Flavor 2: " + str(f2))
            if f1 is not f2:
                x = f1 + 1
                y = f2 + 1
                z = (min(x,y),) + (max(x,y),)
                #print (str(z[0]+str(z[1]))) #print (str(z))
                return z
            elif (len(str(f1)) > 1):
                x = f1[0] + 1
                y = f1[1] + 1
                z = (min(x,y),) + (max(x,y),)
                #print (str(z[0]+str(z[1])))
                return z

def main():
    t = int(input())
    stacks = []
    for t_itr in range(t):
        money = int(input())
        n = int(input())
        cost = list(map(int, input().rstrip().split()))
        stack = whatFlavors(cost, money)
        #print(str(stack[0])+" "+str(stack[1]))
        print("{} {}".format(stack[0], stack[1]))
        stacks.append(stack)

    return stacks

if __name__ == '__main__':
    main()
