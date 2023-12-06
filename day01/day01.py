import re


def solve(lines: list):
    p1, p2 = [], []

    nummap = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    i = [re.findall(r"\d", x) for x in lines]
    p1 = [int(x[0] + x[-1]) for x in i]

    re_l = r"\d|one|two|three|four|five|six|seven|eight|nine"
    re_r = r"\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin"
    lhs = [re.search(re_l, x).group() for x in lines]
    rhs = [re.search(re_r, x[::-1]).group()[::-1] for x in lines]
    p2 = [nummap[x[0]] * 10 + nummap[x[-1]] for x in zip(lhs, rhs)]

    return sum(p1), sum(p2)


if __name__ == "__main__":
    # print(solve([line.strip() for line in open("test2.txt").readlines()]))
    print(solve([line.strip() for line in open("input.txt").readlines()]))

