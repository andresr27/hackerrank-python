#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def rotLeft(a,d):
#    for i in range(d):
#        a0 = a[0]
#        for i in range(n):
#            if i == (n-1):
#                a[i]=a0
#            else:
#                a[i] = a[i+1]
    return a[d:]+a[:d]
if __name__ == '__main__':
    n = 5
    d = 4
    a = [1, 2, 3, 4, 5]
    result = rotLeft(a, d)
    print(result)
