#sol01.py
import sys

def solution1(inputfile: str):
    sum = 0
    for line in open(inputfile).readlines():
        o = ''
        for char in line:
            if char.isdigit():
                o += char
        sum += int(o[0] + o[-1])
    return sum


def evalnumber(input: str):
    if len(input) == 0:
        return 0
    if input[0].isdigit():
        return input[0]
    elif input.startswith("one"):
        return '1'
    elif input.startswith("two"):
        return '2'
    elif input.startswith("three"):
        return '3'
    elif input.startswith("four"):
        return '4'
    elif input.startswith("five"):
        return '5'
    elif input.startswith("six"):
        return '6'
    elif input.startswith("seven"):
        return '7'
    elif input.startswith("eight"):
        return '8'
    elif input.startswith("nine"):
        return '9'
    else:
        return 0

def solution2(inputfile: str):
    sum = 0
    for line in open(inputfile).readlines():
        left, right = 0, 0
        i = 0
        while True:
            if left == 0:
                left = evalnumber(line.strip()[i:]) 
                i += 1
            else:
                break
        i = -1
        while True:
            if right == 0:
                right = evalnumber(line.strip()[i:])
                i -= 1
            else:
                break
        sum += int(left + right)
    return sum

        
if __name__ == "__main__":
    print(f"Test input 1: {solution1("day01_test1.txt")}")
    print(f"Test input 2: {solution2("day01_test2.txt")}")

    print(f"Real input 1: {solution1("day01_input.txt")}")
    print(f"Real input 2: {solution2("day01_input.txt")}")

