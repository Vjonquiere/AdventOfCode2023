def get_input(filePath:str):
    return open(filePath, "r")

def parse(inputFile):
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
        if digit[1] == -1:
            digit[1] = digit[0]
        total += digit[0]*10 + digit[1]
        
    return total

print(parse(get_input("input")))