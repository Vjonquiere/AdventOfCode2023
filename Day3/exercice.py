NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def get_input(filePath:str):
    return open(filePath, "r")

def parse(file):
    lines = file.readlines()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if j == 0 or lines[i][j] in NUMBERS:
                next = lines[i][j+1]
                if (lines[i][j-1] in NUMBERS or lines[i][j-1] == "." or j==0) and (lines[i-1][j] == "." or i==0) and (lines[i+1][j] == "." or i==len(lines)-1) and 
