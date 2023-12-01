STR_TO_INT = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
SPELLED_INT = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def get_input(filePath:str):
    return open(filePath, "r")

def find_last_occurence_index(string:str, substring:str):
    last_index = string.find(substring)
    for i in range(len(string)):
        if string.find(substring, i) != -1:
           last_index = string.find(substring, i)
    return last_index
    

def parse(inputFile, secondPart=False):
    total = 0
    lines = inputFile.readlines()
    for line in lines:
        digit = [-1,-1]
        for letter in line:
            try:
                value = int(letter)
                if digit[0] == -1:
                    digit[0] = value
                else:
                    digit[1] = value
            except:
                pass
        
        if secondPart:
            indexes = [100000, -1]
            word = ["",""]
            
            for number in SPELLED_INT:
                if number in line:
                    if line.find(number) != -1 and line.find(number) < line.find(str(digit[0])) and line.find(number) < indexes[0]:
                        word[0] = number
                        indexes[0] = line.find(number)
                        if digit[1] == -1:
                            digit[1] = digit[0]
                    if find_last_occurence_index(line, number) != -1 and find_last_occurence_index(line, number) > find_last_occurence_index(line, str(digit[1])) and find_last_occurence_index(line, number) > indexes[1] :
                        word[1] = number
                        indexes[1] = find_last_occurence_index(line, number)
            
            if word[0] != "":
                digit[0] = STR_TO_INT[word[0]]
            if word[1] != "":
                digit[1] = STR_TO_INT[word[1]]
        if digit[1] == -1:
            digit[1] = digit[0]

        total += digit[0]*10 + digit[1]
        
    return total

print("Part 1:", parse(get_input("input")))
print("Part 2:", parse(get_input("input"), True))


 ## 55935
 ## 55901
 ## 55301


 ## 4ninecjzlk7nine
 ## 5sixtnthdqksseven5