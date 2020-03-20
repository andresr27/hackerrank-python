from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return '{} {}'.format(self.name, self.score)

    def comparator(self, other):
        if self.score == other.score:
                return 1 if self.name > other.name else -1
        return 1 if self.score < other.score else -1

def main():
    n = int(input())
    data = []
    for i in range(n):
        name, score = input().split()
        score = int(score)
        player = Player(name, score)
        data.append(player)

    data = sorted(data, key=cmp_to_key(Player.comparator))
    for i in data:
        print(i.name, i.score)

if __name__ == '__main__':
    main()
