#May be improved in the future to support "infinite" tape behaviour

class Head:

    def __init__(self, initState, behaviourSet):
        self.state = initState
        self.output = ""
        self.direction = ""
        self.behaviourSet = behaviourSet
        self.problemSolved = False

    def searchBehaviourSet(self, currentState, tapeFedInput):
        for i in range(0, len(self.behaviourSet)):
            if self.behaviourSet[i][0] == currentState and self.behaviourSet[i][1] == tapeFedInput:
                return self.behaviourSet[i]

    def observeTape(self, datum):
        self.singleInstruction = self.searchBehaviourSet(self.state, datum)
        if self.singleInstruction[4] == "HALT":
            self.problemSolved = True
        else:
           self.output = self.singleInstruction[3]
           self.direction = self.singleInstruction[4]

    def writeToTape(self):
        return self.output

    def moveHead(self):
        return self.direction

    def halt(self):
        return self.problemSolved

class Tape:

    def __init__(self, leftData, centreDatum, rightData):
        self.leftData = leftData
        self.centreDatum = centreDatum
        self.rightData = rightData
        self.currentIndex = 0 # make it the index of what ever the centre datum would be

    def stitchTape(self):
        self.singleTape = self.leftData + self.centreDatum
        self.currentIndex = [len(self.singleTape)-1, self.centreDatum[0]]
        self.singleTape = self.singleTape + self.rightData

    def writeToTape(self, newData):
        self.singleTape[self.currentIndex[0]] = newData
        self.currentIndex[1] = newData

    def moveHead(self, direction):
        if direction == "R":
            self.currentIndex[0] += 1
            self.currentIndex[1] = self.singleTape[self.currentIndex[0]]
        elif direction == "L":
            self.currentIndex[0] += 1
            self.currentIndex[1] = self.singleTape[self.currentIndex[0]]

    def showDatum(self):
        return self.currentIndex[1]

    def __str__(self):
        return str(self.singleTape)

def runMachine(head, tape):
    tape.stitchTape()
    while not head.halt():
        print()
        print(tape, tape.currentIndex)
        head.observeTape(tape.showDatum())
        if head.problemSolved == True:
            break
        tape.writeToTape(head.writeToTape())
        tape.moveHead(head.moveHead())
        print()
        print(tape, tape.currentIndex)
    print("Problem Solved")


if __name__ == "__main__":
    machineRuleSet = ( ("S1", "0", "S1", "0", "R"), ("S1", "□", "S0", "□", "HALT"), ("S1", "1", "S0", "0", "R") )
    head = Head("S1",  machineRuleSet)

    leftTapeComponent = ["0" , "0", "1", "0", "1", "0"]
    centreTapeComponent = ["1"]
    rightTapeComponent = ["0" , "0", "1", "0", "0", "0", "□"]
    tape = Tape(leftTapeComponent, centreTapeComponent, rightTapeComponent)


    runMachine(head, tape)
