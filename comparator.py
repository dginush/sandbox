from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return "Player ({0},{1})".format(self.name, self.score)

    def __str__(self):
        return self.__repr__()

    def comparator(self, b):
        if self.score > b.score:
            return -1
        elif self.score == b.score and self.name < b.name:
            return -1
        return 0


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
