#!/usr/bin/python3

import math
import os
import re
import sys
#mod = (10 ** 8)
mod = (10 ** 9)+7
cacheT = {}
#cacheS = {}
s_vec = [2,2,-2,1]
allowed_transitions = set([
  (0,0), (0,2), (2,1), (0,8), (0,7), (7,1),
  (1,1), (1,4), (4,0),
  (2,4), (3,6), (4,5), (4,7), (4,8),
  (4,2), (6,3), (5,4), (7,4), (8,4)
])
def tCount(pos,out,width):
  elem = (pos, out, width)

  if elem in cacheT:
    return cacheT[elem]
  if width == 1:
    if (pos, out) in allowed_transitions:
      return 1
    else:
      return 0
  r = 0
  left_rec = width // 2
  right_rec = width - left_rec
  for i in range(8):
    comb = tCount(pos, i, left_rec) * tCount(i, out, right_rec)
    r += comb
    r = r % mod
  #res = res % mod
  cacheT[elem] = r
  return r

def tMin(n):
    r = tCount(m,8,n)
    print ("T  of:", n, "", r )
    return r

# def sCount(m_min,m,n):
#     r=0
#     #elem = (m,n)
#     #if elem in cacheS:
#     if n > 2 :
#         r = tMin(n+1) - tMin(n) - tMin(n-1) + 3*tMin(n-2) + tMin(n-3) - 2*tMin(n-4)
#     else:
#         r = n
#
#     return r
#
def sCount(m_min,m,n):
     #elem = (m,n)
     #if elem in cacheS:
    #     return cacheS[elem]
     r=0
     if n > 1:
         r += sCount(m_min,m,n-1) + tCount(m_min,m,n)
     elif n == 1: r= 1
     else: r = 0
     r = r % mod
     #cacheS[elem] = r
     return r

def sMin(n):
    return sCount(m_min,m,n)

def sCount2(n):
     r=0
     if n > 1:
         r = 2*sMin(n-1) + 2*sMin(n-2) - 2*sMin(n-3) + sMin(n-4) + 2*sMin(n-5) - 2*sMin(n-6) - 8*sMin(n-7) + 2*sMin(n-9) - 2*sMin(n-10)
     elif n == 1: r= 1
     else: r = 0
     #r = r % mod
     return r

if __name__ == '__main__':
    global m
    global m_min
    m_min = 4
    m = 8

    n = 99


    #n = 5*10**2
    #m = int(input())
    #n = int(input())
    result = sMin(n)
    print (result)
