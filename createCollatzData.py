import csv

commands = {}
# 0 if /2 1 if 3*n+1
numberStepsUntilLower = {}


def addCommands(n, oN):
    global commands
    newN = 0
    if oN not in commands:
        commands[oN] = ""
    if n == 1:
        commands[oN] += "-1"
        return
    elif n % 2 == 0:
        commands[oN] += "0"
        newN = n/2
    elif n % 2 == 1:
        commands[oN] += "1"
        newN = 3*n+1
    addCommands(newN, oN)


def getNumSteps(n):
    global numberStepsUntilLower
    steps = 0
    newN = n
    if n == 1:
        numberStepsUntilLower[n] = -1
    for i in commands[n]:
        if newN % 2 == 0:
            newN /= 2
        elif newN % 2 == 1:
            newN = newN*3+1
        steps += 1
        if newN < n:
            numberStepsUntilLower[n] = steps
            return
    return


def createData():
    data = [
            ["n", "commands", "number steps until lower"]
    ]
    for i in range(1, 1000000):
        addCommands(i, i)
        getNumSteps(i)
        data.append([i, commands[i], numberStepsUntilLower[i]])
    return data


def saveToCSV():
    data = createData()
    with open("data.csv", mode = "w", newline='') as fi:
        wri = csv.writer(fi)
        wri.writerows(data)


saveToCSV()
