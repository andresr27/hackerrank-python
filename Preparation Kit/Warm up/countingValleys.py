#!/usr/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(n, s):
    level = 0
    dstep = 0
    valley_count = 0
    enter_valley = False
    for i in range(n):
        if s[i] == "D":
            dstep = -1
        else:
            dstep = 1

        level += dstep
        print (level, dstep)

        if level < 0:
            enter_valley = True
        else:
            if enter_valley:
                valley_count += 1
                enter_valley = False

    return valley_count
    #

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #n = int(raw_input())
    #p = int(raw_input())
    n = 12
    s = 'DDUUDDUDUUUD'
    result = countingValleys(n, s)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()
