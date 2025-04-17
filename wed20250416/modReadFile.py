def readFile(fileName):
    openfile = open(fileName, 'r')

    print(f'From "{fileName}":')
    line1 = openfile.readline()
    while line1 != '':
        print(line1.strip())
        line1 = openfile.readline()
    
    openfile.close()