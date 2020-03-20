#!/usr/bin/python3
def build_dict_table(keys):
    hash_map = {}
    for key in zip(keys):
        hash_key = key[0]
        if hash_key in hash_map:
            values = hash_map[hash_key] + 1
            hash_map[hash_key] = values
        else:
            hash_map[hash_key] = 1
    return hash_map

def get_value(hash_map, key):
    if key in hash_map:
        values = hash_map[key]
        return values
    else:
        return None


def isValid(s):
    #st = [s[i] for i in range(len(s))]
    #print("String: " + str(st))
    table = build_dict_table(s)
    print("Table: " + str(table))
    reps = 0
    not_modified = True
    for key in table.keys():
        val = get_value(table,key)

        if val is not None:
            print("Mod: " + str(not_modified) + " Char: " + str(key) + "  Val: " + str(val)+ "  Reps: " + str(reps))
            if val != reps:
                ## all good
                if (reps == 0):
                    reps = val
                elif not_modified: #and ((val-1 == reps) or (val +1 == reps)):
                        not_modified = False
                        table[key] = reps
                        #print("Modified: Char: " + str(key) + "  Val: " + str(val)+ "  Reps: " + str(reps))
                else:
                    #print("Char: " + str(key) + "  Val: " + str(val)+ "  Reps: " + str(reps))
                    return "NO"
    return "YES"
    #min(count1,count2)


def main():
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    print(result)
    return result
    # fptr.write(result + '\n')
    # fptr.close()

if __name__ == '__main__':
    main()
