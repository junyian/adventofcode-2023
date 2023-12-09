from collections import Counter


def extrapolate(numlist: list):
    diffs = []
    for i in range(1, len(numlist)):
        diffs.append(numlist[i] - numlist[i - 1])
    stats = Counter(diffs)
    if len(stats) == 1:
        return numlist[-1] + list(stats.keys())[0]
    else:
        return numlist[-1] + extrapolate(diffs)


def solve(lines: list):
    p1, p2 = 0, 0

    history = [x.split() for x in lines]
    for h in history:
        h = [int(x) for x in h]
        p1 += extrapolate(h)
        p2 += extrapolate(h[::-1])
    return p1, p2


if __name__ == "__main__":
    print(solve([line.strip() for line in open("test.txt").readlines()]))
    print(solve([line.strip() for line in open("input.txt").readlines()]))

