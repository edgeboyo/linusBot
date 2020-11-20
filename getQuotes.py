import random

def seperate(isLong):
    l = []
    with open("rants.tsv", "r") as f:
        for line in f:
            l.append(line.split("\t"))
    l = [x[5] for x in l]

    shortR = []
    longR = []

    for i in l:
        if len(i) > 350:
            longR.append(i)
        else:
            shortR.append(i)

    if isLong:
        l = longR
    else:
        l = shortR

    return l

def getRandom(isLong):
    l = seperate(isLong)
    l = l[random.randint(0, len(l)-1)]
    if l[0] == '"':
        l = l[1:]
    if l[-1] == '"':
        l = l[:-1]
    return l


if __name__ == "__main__":
    l = seperate()
    for i in l:
        print(i)