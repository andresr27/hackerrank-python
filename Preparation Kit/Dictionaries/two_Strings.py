#!/usr/bin/python3

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    st1_char_set = []
    for i in range(128):
        if chr(i) in s1:
            st1_char_set.append(chr(i))
    for i in st1_char_set:
        if i in s2: return "YES"
    return "NO"

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        print (str(result) + '\n')
