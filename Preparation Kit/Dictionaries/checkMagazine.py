#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    s=note
    l=magazine
    #s=sorted(note,key=1)
    #l=sorted(magazine)
    if len(s) == len(l):
        s=sorted(note)
        l=sorted(magazine)
        n=0
        is_subset=False
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i+n] == s[n]):
                    n += 1
                if n == len(s):
                    can_do = "Yes"
                else:
                    can_do = "No"
                    break

    else:
        for i in note:
            word_found=False
            #print("Word",i)
            #print (l)
            if s.count(i) <= l.count(i):
                    word_found= True

            if word_found: can_do= "Yes"
            else:
                can_do= "No"
                break
    print(can_do)

    # s=note
    # l=magazine
    #
    # n=0
    # is_subset=False
    # for i in range(len(l)):
    #     for j in range(len(s)):
    #         if l[i] ==  s[j]:
    #             n +=1
    #             l[i] = ""
    # if n == len(s):
    #     is_subset=True
    #
    #
    # if is_subset :
    #     print("Yes")
    # else: print ("No")
    #




if __name__ == '__main__':

    #print ("what's this?")
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()

    checkMagazine(magazine, note)
