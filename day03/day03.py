import re


def evalSchematic1(schematic, maxrow: int, maxcol: int):
    sum = 0
    for rownum, row in enumerate(schematic):
        partnumbers = re.finditer(r"(\d+)", row)
        for partnumber in partnumbers:
            number, startcol, endcol = (
                partnumber.group(),
                partnumber.start(),
                partnumber.end(),
            )
            # Find adjacent symbols
            # Left side
            if startcol > 0:
                if schematic[rownum][startcol - 1] != ".":
                    sum += int(number)
                    continue
            # Right side
            if endcol < maxcol:
                if schematic[rownum][endcol] != ".":
                    sum += int(number)
                    continue
            # Top side
            if rownum > 0:
                for col in range(startcol, endcol):
                    if schematic[rownum - 1][col] != ".":
                        sum += int(number)
                        break
            # Bottom side
            if rownum < maxrow - 1:
                for col in range(startcol, endcol):
                    if schematic[rownum + 1][col] != ".":
                        sum += int(number)
                        break
            # Diagonal top left
            if rownum > 0 and startcol > 0:
                if schematic[rownum - 1][startcol - 1] != ".":
                    sum += int(number)
                    continue
            # Diagonal bottom left
            if rownum < maxrow - 1 and startcol > 0:
                if schematic[rownum + 1][startcol - 1] != ".":
                    sum += int(number)
                    continue
            # Diagonal top right:
            if rownum > 0 and endcol <= maxcol - 1:
                if schematic[rownum - 1][endcol] != ".":
                    sum += int(number)
                    continue
            # Diagonal bottom right:
            if rownum < maxrow - 1 and endcol <= maxcol - 1:
                if schematic[rownum + 1][endcol] != ".":
                    sum += int(number)
                    continue
    return sum


def evalSchematic2(schematic, maxrow, maxcol):
    sum = 0
    for rownum, row in enumerate(schematic):
        for colnum, col in enumerate(row):
            if col == "*":
                # find adjacent partnumbers
                # same row
                gearratio = 0
                partnumbers = re.finditer(r"(\d+)", row)
                for partnumber in partnumbers:
                    number, startcol, endcol = (
                        partnumber.group(),
                        partnumber.start(),
                        partnumber.end(),
                    )
                    # left
                    if colnum == endcol:
                        if gearratio > 0:
                            gearratio *= int(number)
                            sum += gearratio
                            continue
                        else:
                            gearratio = int(number)
                    # right
                    if colnum == startcol - 1:
                        if gearratio > 0:
                            gearratio *= int(number)
                            sum += gearratio
                            continue
                        else:
                            gearratio = int(number)
                # above row
                if rownum > 0:
                    partnumbers = re.finditer(r"(\d+)", schematic[rownum - 1])
                    for partnumber in partnumbers:
                        number, startcol, endcol = (
                            partnumber.group(),
                            partnumber.start(),
                            partnumber.end(),
                        )
                        # diagonal left
                        if colnum == endcol:
                            if gearratio > 0:
                                gearratio *= int(number)
                                sum += gearratio
                                continue
                            else:
                                gearratio = int(number)
                        # diagonal right
                        if colnum == startcol - 1:
                            if gearratio > 0:
                                gearratio *= int(number)
                                sum += gearratio
                                continue
                            else:
                                gearratio = int(number)
                        # above
                        if colnum >= startcol and colnum < endcol:
                            if gearratio > 0:
                                gearratio *= int(number)
                                sum += gearratio
                                continue
                            else:
                                gearratio = int(number)
                # below row
                if rownum < maxrow - 1:
                    partnumbers = re.finditer(r"(\d+)", schematic[rownum + 1])
                    for partnumber in partnumbers:
                        number, startcol, endcol = (
                            partnumber.group(),
                            partnumber.start(),
                            partnumber.end(),
                        )
                        # diagonal left
                        if colnum == endcol:
                            if gearratio > 0:
                                gearratio *= int(number)
                                sum += gearratio
                                continue
                            else:
                                gearratio = int(number)
                        # diagonal right
                        if colnum == startcol - 1:
                            if gearratio > 0:
                                gearratio *= int(number)
                                sum += gearratio
                                continue
                            else:
                                gearratio = int(number)
                        # below
                        if colnum >= startcol and colnum < endcol:
                            if gearratio > 0:
                                gearratio *= int(number)
                                sum += gearratio
                                continue
                            else:
                                gearratio = int(number)
    return sum


def part1(inputfile: str):
    lines = open(inputfile).readlines()
    lines = [line.strip() for line in lines]
    return evalSchematic1(lines, len(lines), len(lines[0]))


def part2(inputfile: str):
    lines = open(inputfile).readlines()
    lines = [line.strip() for line in lines]
    return evalSchematic2(lines, len(lines), len(lines[0]))


if __name__ == "__main__":
    print(f"Test input 1: {part1("test.txt")}")
    print(f"Test input 2: {part2("test.txt")}")
    print(f"Real input 1: {part1("input.txt")}")
    print(f"Real input 2: {part2("input.txt")}")

