def writeFile(fileName):
    openfile = open(fileName, 'w')

    line1 = openfile.write(input('What do you want to write? Type "x" to stop: ') + '\n')
    while line1 != "x":
        line1 = openfile.write(input('What do you want to write? Type "x" to stop: ') + '\n')
    
    openfile.close()