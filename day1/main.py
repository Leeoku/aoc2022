def read_integers(path):
    with open(path,'r') as file:
        elves=[]
        elf = []
        content=file.read()
        for i in content.split('\n'):
            if (i != ''):
                elf.append(int(i))
                # print(elf)
            elif (i == ''):
                elves.append(sum(elf))
                elf = []
            # print(elf)
            
        # print(elves.sort(reverse=True))
    return sorted(elves, reverse=True)

def findMaxElf(elfVal):
    # print(elfVal[0])
    return elfVal[0]

def findTopThreeElves(elfVal):
    elfTotal = sum(elfVal[0:3])
    print(elfVal[0:3])
    print(elfTotal)
    
if __name__ == "__main__":
    values = read_integers("data.txt")
    highest = findMaxElf(values)
    threeHighest = findTopThreeElves(values)
