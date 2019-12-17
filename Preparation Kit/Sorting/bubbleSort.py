#!/usr/bin/python3

# Complete the twoStrings function below.
def countSwaps(a):
    n = len(a)
    count = 0
    for i in range(1,n):
        j=i
        for j in range(n - 1):
            if (a[j] > a[j+1]) :
                a[j],a[j+1] = a[j+1],a[j]
                count += 1
                #print (count, "    ", a)
    print("Array is sorted in", count, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[n-1])


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
