#!/usr/bin/python3

from __future__ import print_function
import os
import sys

def pageCount(n, p):
    #
    # Write your code here.
    if n%2 > 0 :
        a = (n-p)//2
    else:
        a = (n-p+1)//2
    b = p//2
    print (a)
    print (b)

    return min(a,b)
    #

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #n = int(raw_input())
    #p = int(raw_input())
    n = 5
    p = 4
    result = pageCount(n, p)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()
