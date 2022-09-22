#   Author:     Michael Fessler
#   Date:       2022/09/21
#   Version:    0.1
#               Reads input prompts, checks for correct inputs, and then prints the corresponding grades to console

while True:
    testInp = input("Enter your achieved points for the test: ")
    if not testInp.isdigit():
        print("Input error. Please enter a valid integer between 0 and 20! ")
    elif testInp.isdigit():
        numTest = int(testInp)
        if 0 <= numTest <= 20:
            break
        else:
            print("Input error. Please enter a valid integer between 0 and 20! ")

while True:
    examInp = input("Enter your achieved points for the prüfung: ")
    if not examInp.isdigit():
        print("Input error. Please enter a valid integer between 0 and 70! ")


    #        examInp = input("Enter your achieved points for the prüfung: ")
    #        if examInp.isdigit():
    #            numExam = int(examInp)
    #            if 0 <= numExam <= 70:
    #                presInp = input("Did you attend the mündliche präsentation? ")
    #                if presInp == "yes":
    #                    presNumInp = input("Enter your achieved points for the verbal presentation: ")
    #                    if presNumInp.isdigit():
    #                        numPres = int(presNumInp)
    #                        if 0 <= numPres <= 10:
    #                            sumOfPoints = numTest + numExam + numPres
    #                            if 0 <= sumOfPoints < 50:
    #                                grade = "Nicht Genügend (5)"
    #                            elif 50 <= sumOfPoints < 65:
    #                                grade = "Genügend (4)"
    #                            elif 65 <= sumOfPoints < 80:
    #                                grade = "Befriedigend (3)"
    #                            elif 80 <= sumOfPoints < 90:
    #                                grade = "Gut (2)"
    #                            elif 90 <= sumOfPoints <= 100:
    #                                grade = "Sehr Gut (1)"
    #                            else:
    #                                print("Unknown error")
    #                            print("Out of 100 possible points you scored: " + str(sumOfPoints))
    #                            print("Based on your input your grade will be: " + grade)