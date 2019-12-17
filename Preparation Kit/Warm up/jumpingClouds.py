#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    r = 0
    b = set(list(ar))
    for i in b:
        if ar.count(i)//2 >= 1:
            r += (ar.count(i)//2)
    return r


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #n = int(raw_input())
    #ar = map(int, raw_input().rstrip().split())
    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    result = sockMerchant(n, ar)
    print(result)

    #fptr.write(str(result) + '\n')
    #fptr.close()
