if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list_arr = list(arr)
    rup = min(list_arr)
    list_max = max(list_arr)
    for i in list_arr:
        if (i > rup) and (i < list_max):
            rup = i
    print(rup)