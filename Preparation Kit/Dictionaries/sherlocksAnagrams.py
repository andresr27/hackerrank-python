#!/usr/bin/python3
# import string
# import random
# import re
# import math
# import os
# import sys

# Complete the twoStrings function below.
def sherlockAndAnagrams(s):
    n = len(s)
    count = 0
    for l in range(1,n):
        reg = {}
        for i in range(n - l + 1):
            a = list(s[i:i+l])
            a.sort()
            a = ''.join(a)
            if a in reg:
                reg[a] += 1
            else:
                reg[a] = 1
            count += reg[a]-1
    return count

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        print (result , '\n')
