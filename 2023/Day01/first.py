zbroj = 0

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        res = [int(i) for i in line if i.isdigit()]
        tmp = str(res[0]) + str(res[-1])
        zbroj += int(tmp)

print(zbroj)