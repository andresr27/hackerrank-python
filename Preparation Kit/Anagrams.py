#!/usr/bin/python3

def anagram(s):
    count = 0
    char_set = []
    if len(s)%2 != 0:
        return -1
    else:
        a = (s[:(len(s)//2)])
        b = (s[(len(s)//2):])
        c = sorted(a)
        d = sorted(b)

    for i in range(128):
        if chr(i) in a:
            char_set.append(chr(i))

    for j in char_set:
        if c.count(j) > d.count(j) :
                count += c.count(j) - d.count(j)
        elif c.count(j) > d.count(j):
            count += c.count(j) - d.count(j)

    return count
   
if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        print ('\n')
        result = anagram(s)
        print (str(result) + '\n')


