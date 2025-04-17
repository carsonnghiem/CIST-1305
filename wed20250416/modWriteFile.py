def writeFile(fileName):
    openfile = open(fileName, 'w')

    user_input = (input('What do you want to write? Type "x" to stop: '))
    while user_input != "x":
        openfile.write(user_input + '\n')
        user_input = (input('What do you want to write? Type "x" to stop: '))

    openfile.close()