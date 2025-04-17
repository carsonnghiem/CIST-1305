import modReadFile
import modWriteFile

def main():
    decision = input("Do you want to [write] into or [read] a file?: ")

    match decision:
        case "write":
            getWrite()
        case "read":
            getRead()
        case _:
            print('Please input either "write" or "read" exactly!')


def getWrite():
    fileName = input("What file name do you want to write into?: ")
    modWriteFile.writeFile(fileName)
    line1 = modReadFile.readFile(fileName)

    print(f'From "{fileName}":')
    print(line1)

def getRead():
    fileName = input("What file name do you want to read from?: ")
    line1 = modReadFile.readFile(fileName)
    
    print(f'From "{fileName}":')
    print(line1)


main()