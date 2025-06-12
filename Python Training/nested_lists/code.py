from itertools import permutations

def main():
    scores_list = []
    scores= {}

    # Transform to dict
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores[name] = score

    # Remove min
    min_score = min(scores.values())
    min_keys = []
    for key in scores.keys():
        if scores[key] == min_score:
            min_keys.append(key)
    for key in min_keys:
        del scores[key]

    # Find second lowest
    min_score = min(scores.values())
    for key in scores.keys():
        if scores[key] == min_score:
            scores_list.append(str(key).strip("\n"))
    scores_list.sort()
    return scores_list


if __name__ == '__main__':
    main()
