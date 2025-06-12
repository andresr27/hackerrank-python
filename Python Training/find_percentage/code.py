from decimal import Decimal

def main():
    n = int(input())
    student_marks = {}
    name =  ""
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    avg_std = float(sum(student_marks[query_name]) / 3)
    avg_rnd = "{:.2f}".format(avg_std)

    return avg_rnd


if __name__ == '__main__':
    main()
