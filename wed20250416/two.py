
def main():
    outfile = open('numbers.txt', 'w')

    num1 = int(input('Enter a number: '))

    outfile.write(str(num1) + '\n')

    outfile.close()
    print('Data written to numbers.txt')

main()