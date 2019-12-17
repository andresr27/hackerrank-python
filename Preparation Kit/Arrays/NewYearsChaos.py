#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def minimumBribes(q):
    r=0
    for i in range(len(q)):
        #print (b[i],r)
        if (q[i]-(i+1)) > 2:
            r="Too chaotic"
            break
        else:
            for j in range(max(0,q[i]-2),i):
                if (q[j]>q[i]):
                    r+=1
    print (r)

if __name__ == '__main__':
    t = 2
    n = 4
    b = [2, 1, 5, 3, 4]
    #b = [1, 2, 5, 3, 7, 8, 6, 4]
    result = minimumBribes(b)
