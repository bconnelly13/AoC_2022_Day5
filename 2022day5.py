import math, string
letters = string.ascii_uppercase
########## DON'T RUN DAY 1 AND DAY 2 TOGETHER (REPEATED VARS) #############

################ Getting and Organizing Input Data ##################
with open("2022day5.txt", "r") as input:
    data = input.read()

directionsIndex = data.index("move")

info = data[:directionsIndex-2]
directions = data[directionsIndex:].splitlines()

numStacks = int(info[len(info)-2])
stacks = []
for i in range(numStacks):
    stack = []
    stacks.append(stack)


rows = info.splitlines()
for row in rows:
    for i in range(len(row)):
        str = row[i]
        if str in letters:
            stackNum = math.floor(i/4)
            stacks[stackNum].append(str)


################ Part 1 ###############
# for dir in directions:
#     splitDir = dir.split()
#     numTimes = int(splitDir[1])
#     oldStackNum = int(splitDir[3])
#     newStackNum = int(splitDir[5])

#     for i in range(numTimes):
#         oldStack = stacks[oldStackNum-1]
#         newStack = stacks[newStackNum-1]
#         toMove = oldStack.pop(0)
#         newStack.insert(0,toMove)

# answer1 = ""
# for stack in stacks:
#     answer1 += stack[0]
# print(answer1)

################## Part 2 ################
for dir in directions:
    splitDir = dir.split()
    cratesNum = int(splitDir[1])
    oldStackNum = int(splitDir[3])
    newStackNum = int(splitDir[5])

    for i in range(cratesNum):
        oldStack = stacks[oldStackNum-1]
        newStack = stacks[newStackNum-1]
        toMove = oldStack.pop(0)
        newStack.insert(i,toMove)

answer2 = ""
for stack in stacks:
    answer2 += stack[0]

print(answer2)




