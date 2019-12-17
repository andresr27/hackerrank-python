#!/usr/bin/python3

def minimumAbsoluteDifference(arr):
        diff = 10**20
        arr = sorted(arr)
        for i in range(len(arr)-1):
            if (arr[i+1] - arr[i]) < diff :
                diff = abs(arr[i+1] - arr[i])
        return diff
    #min(count1,count2)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print (str(result) + '\n')




    #    return -1
