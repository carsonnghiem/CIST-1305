from calc_one import addition, division

def gradeCalc(s1, s2):
    scoreSum = addition(s1, s2)
    testAvg = division(scoreSum, 2)
    return(testAvg)


def main():
    score1 = float(input("Enter the score for Test 1: "))
    score2 = float(input("Enter the score for Test 2: "))

    grade = gradeCalc(score1, score2)

    print(f"Your test average is % {grade:.2f}")

main()
