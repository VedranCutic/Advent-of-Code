import re

umnozak = 0

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        moze = 1
        tmp1 = line.split(";")
        id = int(tmp1[0][5:tmp1[0].index(":")])
        
        pattern = re.compile(r'(\d+) (\w+)')
        matches = pattern.findall(line)

        red = 0
        blue = 0
        green = 0

        for match in matches:
            if(match[1] == "red"):
                if(int(match[0]) > red):
                    red = int(match[0])
            if(match[1] == "green"):
                if(int(match[0]) > green):
                    green = int(match[0])
            if(match[1] == "blue"):
                if(int(match[0]) > blue):
                    blue = int(match[0])
            
        umnozak += red * green * blue

print(umnozak)