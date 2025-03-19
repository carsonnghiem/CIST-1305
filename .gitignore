from calc_one import addition, subtraction, multiplication, division, modulus


def calculator(a, b):
    #Do-Until loop
    loop = 0
    while loop != "end":
        print(f"With these numbers [{a}], [{b}].")
        print("Would you like to [add], [subtract], [multiply], [divide], [mod], or perform [all] actions?")
        print("     Type [end] once finished")
        loop = input()

        if loop == "add":
            print(f"This is the sum of [{a}] + [{b}] = {addition(a, b)}")
        elif loop == "subtract":
            print(f"This is the difference of [{a}] - [{b}] = {subtraction(a, b)}")
        elif loop == "multiply":
            print(f"This is the product of [{a}] * [{b}] = {multiplication(a, b)}")
        elif loop == "divide":
            print(f"This is the quotient of [{a}] / [{b}] = {division(a, b)}")
        elif loop == "mod":
            print(f"This is the mod of [{a}] % [{b}] = {modulus(a, b)}")
        elif loop == "all":
            print(f"This is the sum of [{a}] + [{b}] = {addition(a, b)}")
            print(f"This is the difference of [{a}] - [{b}] = {subtraction(a, b)}")
            print(f"This is the product of [{a}] * [{b}] = {multiplication(a, b)}")
            print(f"This is the quotient of [{a}] / [{b}] = {division(a, b)}")
            print(f"This is the mod of [{a}] % [{b}] = {modulus(a, b)}")
        elif loop == "end":
            print("--End Task--")
        else:
            print("Please type an appropriate respnose!")
        
        print("----------------------------------------------------------------------------------------------")


def main():
    print("This module will Add, Subtract, Multiply, Divide, and Mod two given numbers.")
    num1 = int(input("Input the first number: "))
    num2 = int(input("Input the second number: "))

    calculator(num1, num2)

main()
