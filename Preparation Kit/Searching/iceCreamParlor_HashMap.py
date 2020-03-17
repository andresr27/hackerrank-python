#!/usr/bin/python3
def build_dict_table(keys,values):
    hash_map = {}
    for key,value in zip(keys,values):
        hash_key = key
        if key in hash_map:
            values = [hash_map[hash_key],value]
            hash_map[hash_key] = values
        else:
            hash_map[hash_key] = value
    return hash_map

def get_value(hash_map, key):
    if key in hash_map:
        values = hash_map[key]
        return values
    else:
        return None

def whatFlavors(costs,money):
    indexes = range(len(costs))
    table = build_dict_table(costs,indexes)
    sorted_costs = sorted(costs)
    for a in costs:
        b = money - a
        f1 = get_value(table, a)
        f2 = get_value(table, b)
        if (f1 is not None) and (f2 is not None):
            if f1 is not f2:
                x = f1 + 1
                y = f2 + 1
                z = (min(x,y),) + (max(x,y),)
                #print (str(z[0]+str(z[1]))) 
                return z
            elif (len(str(f1)) > 1):
                x = f1[0] + 1
                y = f1[1] + 1
                z = (min(x,y),) + (max(x,y),)
                #print (str(z[0]+str(z[1])))
                return z

def main():
    t = int(input())
    stacks = []
    for t_itr in range(t):
        money = int(input())
        n = int(input())
        cost = list(map(int, input().rstrip().split()))
        stack = whatFlavors(cost, money)
        print("{} {}".format(stack[0], stack[1]))
        stacks.append(stack)

    return stacks

if __name__ == '__main__':
    main()
