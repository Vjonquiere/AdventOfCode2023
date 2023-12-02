COLOR_LIST = ["red", "green", "blue"]

def get_input(filePath:str):
    return open(filePath, "r")

def get_game_id(gameID:str) -> int:
    return int(gameID.split(" ")[1])

def countRGB(gameData:str) -> list:
    sets = gameData.split(";")
    parsedLine = []
    for set1 in sets:
        colors = set1.split(",")
        final = {}
        for color in colors:
            value = color.split(" ")
            final[value[2].replace("\n", "")] = value[1]
        parsedLine.append(final)
    return parsedLine

def check_rule(colorSets:list, rule:dict) -> bool:
    for set1 in colorSets:
        for color in COLOR_LIST:
            if color in set1 and int(set1[color]) > rule[color]:
                return False
    return True

def maxColor(colorSets:list):
    red = []
    green = []
    blue = []
    for set1 in colorSets:
        red.append(int(set1["red"])) if "red" in set1 else red.append(0)
        green.append(int(set1["green"])) if "green" in set1 else green.append(0)
        blue.append(int(set1["blue"])) if "blue" in set1 else blue.append(0)
    return {"red":  0 if red == [] else max(red), "green": 0 if green == [] else max(green), "blue": 0 if blue == [] else max(blue)}

def part1(input, rule:dict):
    total = 0
    lines = input.readlines()
    for line in lines:
        data = line.split(":")
        id = get_game_id(data[0])
        colors = countRGB(data[1])
        if check_rule(colors, rule):
            total += id
    return total

def part2(input):
    total = 0
    lines = input.readlines()
    for line in lines:
        data = line.split(":")
        colors = countRGB(data[1])
        mini = maxColor(colors)
        total += mini["red"] * mini["green"] * mini["blue"]
    return total

        


print("Question 1:", part1(get_input("input"), {"red": 12, "green": 13, "blue": 14}))
print("Question 2:", part2(get_input("input")))