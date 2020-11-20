import random

def seperate():
    l = []
    with open("rants.tsv", "r") as f:
        for line in f:
            l.append(line.split("\t"))
    l = [x[5] for x in l]
    return l

def getRandom():
    l = seperate()
    return l[random.randint(0, len(l)-1)]


if __name__ == "__main__":
    l = seperate()
    for i in l:
        print(i)