def solve(lines: list):
    p1, p2 = 1, 1

    time = [int(x) for x in lines[0][lines[0].index(":") + 1 :].split()]
    distance = [int(x) for x in lines[1][lines[1].index(":") + 1 :].split()]
    races = zip(time, distance)
    for race in races:
        d = [a * (race[0] - a) for a in range(1, race[0])]
        d = [x for x in d if x > race[1]]
        p1 *= len(d)

    time = int(lines[0][lines[0].index(":") + 1 :].replace(" ", ""))
    distance = int(lines[1][lines[1].index(":") + 1 :].replace(" ", ""))
    d = [a * (time - a) for a in range(1, time)]
    p2 = len([x for x in d if x > distance])
    return p1, p2


if __name__ == "__main__":
    print(solve([line.strip() for line in open("test.txt").readlines()]))
    print(solve([line.strip() for line in open("input.txt").readlines()]))

