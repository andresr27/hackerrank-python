#!/usr/bin/python3

def takeFirst(elem):
    return elem[0]

def luckBalance(k,contests):


        balance = 0
        imp = []
        n = len(contests)

        # lose all unimportant
        for i in range(n):
            a,b = contests[i]
            if b == 0 :
                balance += a
            else:
                imp.append(a)
        imp = sorted(imp, reverse = True)
        # Lose only the best k contests_sorted
        balance += sum(imp[:min(k,len(imp))])
        # Win the rest of the contests
        balance -= sum(imp[k:])
        return balance

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))
    result = luckBalance(k, contests)
    print (str(result) + '\n')
