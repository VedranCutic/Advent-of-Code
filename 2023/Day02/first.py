import re

zbroj = 0

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        moze = 1
        tmp1 = line.split(";")
        id = int(tmp1[0][5:tmp1[0].index(":")])
        
        pattern = re.compile(r'(\d+) (\w+)')
        matches = pattern.findall(line)

        for match in matches:
            if(match[1] == "red"):
                if(int(match[0]) > 12):
                  moze = 0
            if(match[1] == "green"):
                if(int(match[0]) > 13):
                    moze = 0
            if(match[1] == "blue"):
                if(int(match[0]) > 14):
                    moze = 0
        
        if(moze == 1):
            zbroj += int(id)
    
print(zbroj)