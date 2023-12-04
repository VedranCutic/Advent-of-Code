zbroj = 0

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        tmp = line
        if "two" in tmp:
            tmp = tmp.replace("two", "two2two")
        if "one" in tmp:
            tmp = tmp.replace("one", "one1one")    
        if "three" in tmp:
            tmp = tmp.replace("three", "three3three")
        if "four" in tmp:
            tmp = tmp.replace("four", "four4four")
        if "five" in tmp:
            tmp = tmp.replace("five", "five5five")
        if "six" in tmp:
            tmp = tmp.replace("six", "six6six")
        if "seven" in tmp:
            tmp = tmp.replace("seven", "seven7seven")
        if "nine" in tmp:
            tmp = tmp.replace("nine", "nine9nine")
        if "eight" in tmp:
            tmp = tmp.replace("eight", "eight8eight")
        res = [int(i) for i in tmp if i.isdigit()]
        tmp2 = str(res[0]) + str(res[-1])
        zbroj += int(tmp2)

print(zbroj)