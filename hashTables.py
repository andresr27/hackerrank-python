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

        #keys = range(n)
        #values = costs
        #hash = {k:v for k, v in zip(keys, values)}
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
        return x,y

def main():
    t = int(input())
    stacks = []
    for t_itr in range(t):
        money = int(input())
        n = int(input())
        cost = list(map(int, input().rstrip().split()))
        stack = whatFlavors(cost, money)
        stacks.append(stack)
    return stacks

if __name__ == '__main__':

    main()
