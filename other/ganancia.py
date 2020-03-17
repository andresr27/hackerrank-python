#!/usr/bin/python3
def ganancia(a):
    return max(a) - a[0]

def main():
    n = input()
    a = [int(n) for n in input().strip().split()]
    #print("inputs " + str(n) + " " + str (a))
    result = ganancia(a)
    print(result)
    return result

if __name__ == '__main__':
    main()
