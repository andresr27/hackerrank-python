#!/usr/bin/python3
import itertools
# Complete the maxSubsetSum function below.


def sumArray(arr):
    sum = 0
    for e in arr:
        sum = sum + e
    return sum

# build a table stores index and value

def get_key(dict,e):
    for key in dict.keys():
        if e == dict[key]:
            return key
    return None

def isValidSubset(dict,arr):
    if len(arr) > 1:
        indexes = list(range(0,len(arr)))

        for t in list(itertools.combinations(indexes,2)):
            if (get_key(dict,arr[t[1]]) - get_key(dict,arr[t[0]])) < 2:
                return False

        return True
    else: return True

def maxSubsetSum(arr):
    sum = 0
    indexes = range(len(arr))
    dict = {k:v for k,v in zip(indexes,arr)}
    for i in range(len(arr)):
        for subset in itertools.combinations(arr,i):

            if isValidSubset(dict,subset):
                new_sum = sumArray(subset)
                sum = max(sum,new_sum)
    return sum

def main():

    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = maxSubsetSum(arr)
    print(res)
    return res


if __name__ == '__main__':
    main()
