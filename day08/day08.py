import numpy as np
import re


def rl_map(x):
    if x == "L":
        return 0
    else:
        return 1


def parseInput(lines: list):
    instr = list(map(rl_map, lines[0].strip()))

    nodes = {}

    for line in lines[2:]:
        m = re.match(r"(\w+) = \((\w+), (\w+)\)", line)
        node, left, right = m.groups()
        nodes[node] = (left, right)

    return instr, nodes


def solve1(lines: list):
    p1 = 0

    instr, nodes = parseInput(lines)

    curnode = "AAA"
    i = 0
    while curnode != "ZZZ":
        curnode = nodes[curnode][instr[i % len(instr)]]
        i += 1
        p1 += 1
    return p1


def solve2(lines: list):
    p2 = []

    instr, nodes = parseInput(lines)

    startnodes = [x for x in nodes if x[2] == "A"]
    for c, startnode in enumerate(startnodes):
        i = 0
        curnode = startnode
        p2.append(0)
        while curnode[2] != "Z":
            curnode = nodes[curnode][instr[i % len(instr)]]
            i += 1
            p2[c] += 1
    p2 = np.array(p2).astype(np.int64)  # convert to big number
    return np.lcm.reduce(p2)


if __name__ == "__main__":
    print(solve1([line.strip() for line in open("test1.txt").readlines()]))
    print(solve1([line.strip() for line in open("test2.txt").readlines()]))
    print(solve2([line.strip() for line in open("test3.txt").readlines()]))

    print(solve1([line.strip() for line in open("input.txt").readlines()]))
    print(solve2([line.strip() for line in open("input.txt").readlines()]))

