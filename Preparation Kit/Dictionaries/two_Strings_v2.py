#!/usr/bin/python3

# Complete the twoStrings function below.
if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        a = set(input())
        b = set(input())
        if len(a.intersection(b))>0:
            print ("YES")
        else:
            print ("NO")

        #result = twoStrings(s1, s2)
        #print (str(result) + '\n')
