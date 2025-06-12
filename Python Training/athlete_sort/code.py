from decimal import Decimal

def main():
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input().strip())

    joined_arr = [" ".join(str(x) for x in l) for l in sorted(arr, key=lambda x: x[k])]

    return joined_arr


if __name__ == '__main__':
    main()
