import re


def part1(inputfile: str):
    sum = 0
    for lines in open(inputfile).readlines():
        winningnums = re.split(r"\s+", lines[lines.index(":") : lines.index("|")])
        winningnums = [int(n.strip()) for n in winningnums if n.strip().isdigit()]
        mynums = re.split(r"\s+", lines[lines.index("|") :])
        mynums = [int(n.strip()) for n in mynums if n.strip().isdigit()]
        matches = list(set(winningnums) & set(mynums))
        if len(matches) > 0:
            sum += 2 ** (len(matches) - 1)
    return sum


def part2(inputfile: str):
    sum = 0
    cards = {1: 1}

    lines = open(inputfile).readlines()
    # init dict of cards
    for i in range(len(lines)):
        cards[i + 1] = 1

    for i, line in enumerate(lines):
        cardnum = i + 1
        if cardnum not in cards.keys():
            cards[cardnum] = 1
        winningnums = re.split(r"\s+", line[line.index(":") : line.index("|")])
        winningnums = [int(n.strip()) for n in winningnums if n.strip().isdigit()]
        mynums = re.split(r"\s+", line[line.index("|") :])
        mynums = [int(n.strip()) for n in mynums if n.strip().isdigit()]
        matches = list(set(winningnums) & set(mynums))
        for j in range(cardnum + 1, cardnum + len(matches) + 1):
            if j in cards.keys():
                cards[j] += cards[cardnum]  # for every match, add same number of cards
        sum += cards[cardnum]

    return sum


if __name__ == "__main__":
    print(f"Test input 1: {part1("test.txt")}")
    print(f"Test input 2: {part2("test.txt")}")
    print(f"Real input 1: {part1("input.txt")}")
    print(f"Real input 2: {part2("input.txt")}")

