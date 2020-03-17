#!/usr/bin/python3

def sonAmigos(a,b):
    div_a = []
    div_b = []
    for i in range(1,a-1):# innecesary work change to mod2+1?
        if a%i == 0:
            #i is a div
            div_a.append(i)
    for j in range(1,b-1):
        if b%j == 0:
            div_b.append(j)
    if (sum(div_a) == b) and (sum(div_b) == a):
        return True
    else: return False

def main():
    line = input()
    line = line.split(' ')
    a = int(line[0])
    b = int(line[1])
    print("inputs " + str(a) + " " + str (b))
    result = sonAmigos(a,b)
    print(result)
    return result

if __name__ == '__main__':
    main()
