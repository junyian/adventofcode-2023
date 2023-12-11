from pprint import pprint

g_map = []
g_map_max_row = 0
g_map_max_col = 0


def findS():
    s = [
        (x, y)
        for x in range(g_map_max_row + 1)
        for y in range(g_map_max_col + 1)
        if g_map[x][y] == "S"
    ]
    return s[0]


def findPipes(curpos: tuple, positions: list):
    result = []
    for p in positions:
        if len(result) == 2:
            return result
        if p == "t":
            if curpos[0] > 0:
                t_row, t_col = curpos[0] - 1, curpos[1]
                if g_map[t_row][t_col] in ["|", "7", "F"]:
                    result.append(([t_row, t_col], "b"))
        elif p == "b":
            if curpos[0] < g_map_max_row:
                t_row, t_col = curpos[0] + 1, curpos[1]
                if g_map[t_row][t_col] in ["|", "J", "L"]:
                    result.append(([t_row, t_col], "t"))
        elif p == "l":
            if curpos[1] > 0:
                t_row, t_col = curpos[0], curpos[1] - 1
                if g_map[t_row][t_col] in ["-", "L", "F"]:
                    result.append(([t_row, t_col], "r"))
        elif p == "r":
            if curpos[1] < g_map_max_col:
                t_row, t_col = curpos[0], curpos[1] + 1
                if g_map[t_row][t_col] in ["-", "J", "7"]:
                    result.append(([t_row, t_col], "l"))
    return result


def solve(lines: list):
    global g_map
    global g_map_max_row
    global g_map_max_col

    p1, p2 = 1, 1

    g_map = [x.strip() for x in lines]
    g_map_max_row = len(g_map) - 1
    g_map_max_col = len(g_map[0]) - 1

    s = findS()
    pipes = findPipes(s, ["t", "b", "l", "r"])
    while pipes[0][0] != pipes[1][0]:
        p1 += 1
        for i, pipe in enumerate([pipes[0][0], pipes[1][0]]):
            pipe_row, pipe_col = pipe[0], pipe[1]
            if g_map[pipe_row][pipe_col] == "|":
                paths = ["t", "b"]
                paths.remove(pipes[i][1])
                pipes[i] = findPipes(pipes[i][0], paths)[0]
            elif g_map[pipe_row][pipe_col] == "-":
                paths = ["l", "r"]
                paths.remove(pipes[i][1])
                pipes[i] = findPipes(pipes[i][0], paths)[0]
            elif g_map[pipe_row][pipe_col] == "7":
                paths = ["l", "b"]
                paths.remove(pipes[i][1])
                pipes[i] = findPipes(pipes[i][0], paths)[0]
            elif g_map[pipe_row][pipe_col] == "F":
                paths = ["r", "b"]
                paths.remove(pipes[i][1])
                pipes[i] = findPipes(pipes[i][0], paths)[0]
            elif g_map[pipe_row][pipe_col] == "J":
                paths = ["l", "t"]
                paths.remove(pipes[i][1])
                pipes[i] = findPipes(pipes[i][0], paths)[0]
            elif g_map[pipe_row][pipe_col] == "L":
                paths = ["t", "r"]
                paths.remove(pipes[i][1])
                pipes[i] = findPipes(pipes[i][0], paths)[0]

    return p1, p2


if __name__ == "__main__":
    print(solve([line.strip() for line in open("test1.txt").readlines()]))
    print(solve([line.strip() for line in open("test2.txt").readlines()]))

    print(solve([line.strip() for line in open("input.txt").readlines()]))

