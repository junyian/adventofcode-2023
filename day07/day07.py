import functools
from collections import Counter

rank_p1 = "23456789TJQKA"
rank_p2 = "J23456789TQKA"


def evalType_p1(hand: str):
    c = sorted(Counter(hand).items(), key=lambda x: x[1], reverse=True)
    if c[0][1] == 5:
        return 7
    elif c[0][1] == 4:
        return 6
    elif c[0][1] == 3 and c[1][1] == 2:
        return 5
    elif c[0][1] == 3 and c[1][1] == 1:
        return 4
    elif c[0][1] == 2 and c[1][1] == 2:
        return 3
    elif c[0][1] == 2 and c[1][1] == 1:
        return 2
    elif c[0][1] == 1:
        return 1
    else:
        return 0


def evalType_p2(hand: str):
    ctr = Counter(hand)
    c = sorted(ctr.items(), key=lambda x: x[1], reverse=True)
    i = 0

    if c[i][1] == 5:
        return 7

    if c[i][0] == "J":
        i = 1

    if c[i][1] + ctr["J"] == 5:
        return 7
    elif c[i][1] + ctr["J"] == 4:
        return 6
    elif c[i][1] + ctr["J"] == 3 and c[i + 1][1] == 2:
        return 5
    elif c[i][1] + ctr["J"] == 3 and c[i + 1][1] == 1:
        return 4
    elif c[i][1] + ctr["J"] == 2 and c[i + 1][1] == 2:
        return 3
    elif c[i][1] + ctr["J"] == 2 and c[i + 1][1] == 1:
        return 2
    elif c[i][1] + ctr["J"] == 1:
        return 1
    else:
        return 0


def mycmp_p1(val1, val2):
    type1, type2 = evalType_p1(val1[0]), evalType_p1(val2[0])
    if type1 > type2:
        return 1
    elif type2 > type1:
        return -1
    elif type1 == type2:
        z = zip([x for x in val1[0]], [x for x in val2[0]])
        while True:
            v1, v2 = next(z)
            if rank_p1.index(v1) > rank_p1.index(v2):
                return 1
            elif rank_p1.index(v2) > rank_p1.index(v1):
                return -1


def mycmp_p2(val1, val2):
    type1, type2 = evalType_p2(val1[0]), evalType_p2(val2[0])

    if type1 > type2:
        return 1
    elif type2 > type1:
        return -1
    elif type1 == type2:
        z = zip([x for x in val1[0]], [x for x in val2[0]])
        while True:
            v1, v2 = next(z)
            if rank_p2.index(v1) > rank_p2.index(v2):
                return 1
            elif rank_p2.index(v2) > rank_p2.index(v1):
                return -1


def solve(lines: list):
    p1, p2 = 0, 0

    hands = [line.split() for line in lines]
    hands = [[x, int(y)] for x, y in hands]
    pp1 = sorted(hands, key=functools.cmp_to_key(mycmp_p1))
    for i, v in enumerate(pp1):
        p1 += v[1] * (i + 1)

    pp2 = sorted(hands, key=functools.cmp_to_key(mycmp_p2))
    for i, v in enumerate(pp2):
        p2 += v[1] * (i + 1)

    return p1, p2


if __name__ == "__main__":
    print(solve([line.strip() for line in open("test.txt").readlines()]))
    print(solve([line.strip() for line in open("input.txt").readlines()]))

