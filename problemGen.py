import random

#Initalizing seed
random.seed()

class problemSet():
    #Defining the base class

    def __init__(self, s):
        self.steps = (s * 2) - 1 

    #Function that can define operands
    def createOperand(self, num):
        if(num == 1):
            return '+'
        elif(num == 2):
            return '-'
        elif(num == 3):
            return '/'
        elif(num == 4):
            return '*'
        else:
            return -1

class lowerBead(problemSet):
    #Child class

    def __init__(self, s):
        problemSet.__init__(self, s)
        #The structure of "problemSteps" will act like an rpn calculator
        #Number -> Operand -> Number... [3, -, 4, +, 3, -]
        self.problemSteps = []
        self.creatingProblem()

    def creatingProblem(self):
        #Creating the final Answer - the abacaus can only have a max answer of 4 and a min answer of 0
        finalAnswer = []

        counter = 0
        #Creating first problem of the set: The operand is ALWAYS positive, aloha dosent want negative numbers
        self.problemSteps.append(random.randrange(1,5))
        finalAnswer.append(self.problemSteps[0])

        while True:
            testInput = random.randrange(1,5)
            testOperand = self.createOperand(random.randrange(0,3))
            
            if(testOperand == '+'):
                if(((sum(finalAnswer) + testInput) <= 4)):
                    self.problemSteps.append(testOperand)
                    self.problemSteps.append(testInput)
                    finalAnswer.append(testInput)
                    counter = counter + 2
                else:
                    pass

            elif(testOperand == '-'):
                if(((sum(finalAnswer) - testInput) >= 0)):
                    self.problemSteps.append(testOperand)
                    self.problemSteps.append(-1* testInput)
                    finalAnswer.append(-1 * testInput)
                    counter = counter + 2
                else:
                    pass
            else:
                pass
            #Condition for loop
            if(len(self.problemSteps) == self.steps):
                break



