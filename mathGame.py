try:
    import myPythonFunctions as m

    userName = input('Please enter your username: ')

    userScore = int(m.getUserPoint(userName))

    if userScore == -1:
        newUser = True
        userScore = 0
    else:
        newUser = False

    userChoice = 0

    while userChoice != '-1':
        userScore += m.generateQuestion()
        print('Current Score =', userScore)
        userChoice = input('Type -1 for exit or 0 to continue:')

    m.updateUserPoints(newUser, userName, str(userScore))
except Exception as e:
    print('An unexpected error occurred. Program will exit now.')
