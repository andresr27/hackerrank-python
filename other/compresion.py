#!/usr/bin/python3
# Brute Force
def comprimir(a):
    out = ""
    i = 0
    while (i < len(a)):
        old_val = a[i]
        #print ("current out: " + str(i) + "  " + out)
        if (i >= len(a)-1):
            break
        else:
            new_val = a[i+1]
            count = 0
            while (new_val == old_val):
                count = count + 1
                if (i < len(a)-1):
                    i = i + 1
                    new_val = a[i]
                else: break
            if count > 1:
                out = out + str(count) + old_val 
            else:
                out = out + old_val
                i = i + 1
    return out


def main():
    line = input()
    a = line
    #print(a)
    result = comprimir(a)
    print(result)
    return result

if __name__ == '__main__':
    main()
