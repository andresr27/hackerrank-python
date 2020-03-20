#!/usr/bin/python3
def maxSubsetSum(arr):
    #print("Array: " + str(arr))
    sum = []
    sum.append(arr[0])#final_sum = 0
    sum.append((max(sum[0],arr[1])))
    sum.append(max(sum[0],sum[0]+arr[2],arr[2]))

    for i in range(3,len(arr)):
        new_sum = []
        sum1 = 0
        sum1=max(sum[i-2],sum[i-3])
        sum2 = max(sum1,sum1+arr[i],arr[i])
        sum.append(sum2)
    return max(sum)

def main():
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = maxSubsetSum(arr)
    print(res)
    return res
    
if __name__ == '__main__':
    main()
