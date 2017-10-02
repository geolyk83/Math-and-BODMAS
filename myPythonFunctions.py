from random import randint
from os import remove, rename

def getUserPoint(userName):
    try:
        openFile = open('userScores.txt', 'r')

        for line in openFile:
            content = line.split(',')
            if content[0] == userName:
                openFile.close()
                return content[1]

        openFile.close()
        return '-1'
    except IOError:
        print('The txt file is not found. We will create the file now.')

        openFile = open('userScores.txt', 'w')

        openFile.close()
        return '-1'

def updateUserPoints(newUser, userName, score):
    if newUser:
        openFile = open('userScores.txt', 'a')
        openFile.write('\n' + userName + ', ' + score)
        openFile.close
    else:
        openFile = open('userScores.tmp', 'w')
        openfile = open('userScores.txt', 'r')

        for line in openfile:
            content = line.split(',')
            if content[0] == userName:
                content[1] = score
                line = content[0] + ', ' + content[1] + '\n'
            openFile.write(line)
        openFile.close
        openfile.close
        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')

def generateQuestion():
    operandList = [0, 0, 0, 0, 0]
    operatorList = ['', '', '', '']
    operatorDict = {1:'+', 2:'-', 3:'*', 4:'**'}

    for i in range(5):
        operandList[i] = randint(1, 9)

    for i in range(4):
        if i > 0 and operatorList[i-1] == '**':
            operatorList[i] = operatorDict[randint(1, 3)]
        else:
            operatorList[i] = operatorDict[randint(1, 4)]

    questionString = ''

    for i in range(5):
        questionString += str(operandList[i])
        if i < 4:
            questionString += operatorList[i]

    result = eval(questionString)

    questionString = questionString.replace('**', '^')

    print('\nCalculate the mathematical expresion:', questionString)

    userResult = input('Please type your answer here: ')

    while True:
        try:
            if int(userResult) == result:
                print('Amazing!!! You got it right')
                return 1
            else:
                print('Sorry...your answer is wrong.')
                print('The correct answer is:', result)
                return 0
        except Exception as e:
            print('\nError: You did not enter a number. Please try again.')
            userResult = input('Please type your answer here: ')
