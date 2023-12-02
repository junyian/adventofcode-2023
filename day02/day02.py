import re


def part1(inputfile: str):
    sum = 0
    limits = {"red": 12, "green": 13, "blue": 14}

    for line in open(inputfile).readlines():
        match = re.match(r"Game (\d+):(.*)", line)
        # print(match[1], match[2])
        if match:
            gameID = match[1]
            # print(gameID)
            cubes = match[2]
            splits = re.split("[ ,;]", cubes.strip())
            isPossible = True
            for i in range(0, len(splits), 3):
                count = splits[i]
                color = splits[i + 1]
                # print("  ", count, color)
                if limits[color] < int(count):
                    isPossible = False
                    break
            if isPossible:
                # print("  Possible")
                sum += int(gameID)
    return sum


def part2(inputfile: str):
    sum = 0

    for line in open(inputfile).readlines():
        maxcolors = {"red": 0, "green": 0, "blue": 0}
        _, cubes = line.split(":")
        splits = re.split("[ ,;]", cubes.strip())
        for i in range(0, len(splits), 3):
            count = splits[i]
            color = splits[i + 1]
            maxcolors[color] = max(maxcolors[color], int(count))
        power = maxcolors["red"] * maxcolors["green"] * maxcolors["blue"]
        sum += power
    return sum


if __name__ == "__main__":
    print(f"Test input 1: {part1("day02_test1.txt")}")
    print(f"Test input 2: {part2("day02_test1.txt")}")

    print(f"Real input 1: {part1("day02_input.txt")}")
    print(f"Real input 2: {part2("day02_input.txt")}")

