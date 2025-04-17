def readFile(fileName):
    openfile = open(fileName, 'r')

    line1 = openfile.readline()
    while openfile != '':
        print(line1)
        line1 = openfile.readline()
    
    openfile.close()