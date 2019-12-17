#!/usr/bin/python3

def get_index(l,a,b):
    x = []
    y  = 0
    for i in range(len(l)):
        if a == l[i] :
            x.append(i+1)

        elif b == l[i] :
            x.append(i+1)

    return min(x[0],x[1]),max(x[0],x[1])

def whatFlavors(costs,money):
        n = len(costs)
        keys = range(n)
        l = costs
        x = 0
        y = 0
        i = 0
        a = money
        while a > 0:
            a = money - i
            b = money - a
            if a == b and l.count(a) > 1:
                x,y = get_index(l,a,a)
                break
            elif l.count(a) > 0 and l.count(b) >= 1:
                x,y = get_index(l,a,b)
                break
            else : i += 1
        print(x,y)

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        money = int(input())
        n = int(input())
        cost = list(map(int, input().rstrip().split()))
        whatFlavors(cost, money)
