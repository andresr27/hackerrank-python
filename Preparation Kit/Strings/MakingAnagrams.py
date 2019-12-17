#!/usr/bin/python3

def makingAnagram(a,b):
        count = 0
        char_set_a = []
        char_set_b = []

        for i in range(128):
            if chr(i) in a:
                char_set_a.append(chr(i))
            if chr(i) in b:
                char_set_b.append(chr(i))


        for j in char_set_a:
            if a.count(j) > b.count(j) :
                    count += a.count(j) - b.count(j)
        for j in char_set_b:
            if b.count(j) > a.count(j):
                    count += b.count(j) - a.count(j)

        return count
    #min(count1,count2)

if __name__ == '__main__':
        a = input()
        b = input()
        #print ('\n')
        result = makingAnagram(a,b)
        print (str(result) + '\n')




    #    return -1
