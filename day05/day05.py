def parseFile(input):
    seeds = []
    mapping = {
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": [],
    }
    cur_key = ""

    for line in input:
        if line.startswith("seeds:"):
            seeds = [int(x) for x in line[line.index(":") + 1 :].split()]
        elif line.startswith("seed-to-soil"):
            cur_key = "seed-to-soil"
        elif line.startswith("soil-to-fertilizer"):
            cur_key = "soil-to-fertilizer"
        elif line.startswith("fertilizer-to-water"):
            cur_key = "fertilizer-to-water"
        elif line.startswith("water-to-light"):
            cur_key = "water-to-light"
        elif line.startswith("light-to-temperature"):
            cur_key = "light-to-temperature"
        elif line.startswith("temperature-to-humidity"):
            cur_key = "temperature-to-humidity"
        elif line.startswith("humidity-to-location"):
            cur_key = "humidity-to-location"
        else:
            if len(line.strip()) > 0:
                mapping[cur_key].append([int(x) for x in line.split()])

    return seeds, mapping


def getMapping(src: int, mapping):
    for map in mapping:
        if src >= map[1] and src < map[1] + map[2]:
            return src - map[1] + map[0]
    return src


def part1(inputfile: str):
    lines = open(inputfile).readlines()
    seeds, mapping = parseFile(lines)
    result = -1
    for seed in seeds:
        soil = getMapping(seed, mapping["seed-to-soil"])
        fertilizer = getMapping(soil, mapping["soil-to-fertilizer"])
        water = getMapping(fertilizer, mapping["fertilizer-to-water"])
        light = getMapping(water, mapping["water-to-light"])
        temperature = getMapping(light, mapping["light-to-temperature"])
        humidity = getMapping(temperature, mapping["temperature-to-humidity"])
        location = getMapping(humidity, mapping["humidity-to-location"])
        # print(
        #     f"seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}"
        # )
        if location < result or result == -1:
            result = location
    return result


def part2(inputfile: str):
    lines = open(inputfile).readlines()
    seeds, mapping = parseFile(lines)
    result = -1
    for i in range(0, len(seeds), 2):
        for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
            soil = getMapping(seed, mapping["seed-to-soil"])
            fertilizer = getMapping(soil, mapping["soil-to-fertilizer"])
            water = getMapping(fertilizer, mapping["fertilizer-to-water"])
            light = getMapping(water, mapping["water-to-light"])
            temperature = getMapping(light, mapping["light-to-temperature"])
            humidity = getMapping(temperature, mapping["temperature-to-humidity"])
            location = getMapping(humidity, mapping["humidity-to-location"])
            # print(
            #     f"seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}"
            # )
            if location < result or result == -1:
                result = location
    return result


if __name__ == "__main__":
    print(f"Test input 1: {part1("test.txt")}")
    print(f"Test input 2: {part2("test.txt")}")
    print(f"Real input 1: {part1("input.txt")}")
    print(
        f"Real input 2: {part2("input.txt")}"
    )  # bruteforcer is very slow! about 4 hours to complete

