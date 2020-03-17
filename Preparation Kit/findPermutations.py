#!/usr/bin/python3
# form itertools import permutaions

# find all the permutations of s within b

def findPermutations(s,b):
    n = len (s)
    if n == 0:
        return ['']
    prev = findPermutations(s[1:n],b)
    m = len (prev)
    next = []
    for i in range(0,m):
        for j in range(0,n):
            new_s = prev[i][0:j] + s[0] + prev[i][j:n-1]
            if new_s not in next:
                #if new_s in b:
                    next.append(new_s)
    return next

def findSinB(s,b):
    sol = []
    for str in findPermutations(s,b):
        if str in b:
            sol.append(str)
    return sol

if __name__ == '__main__':
    s = input()
    b = input()
    #result = findSinB(s,b)
    result = findPermutations(s,b)
    print (result , '\n')
