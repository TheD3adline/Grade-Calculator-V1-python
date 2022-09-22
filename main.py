#   Author:     Michael Fessler
#   Date:       2022/09/21
#   Version:    0.1
#               Reads input prompts, checks for correct inputs, loops
#               back to the prompt if invalid and then prints the
#               corresponding grades to console

# Asks for input of scored points at the test, is looped and only breaks the loop if a valid input is made
while True:
    testInp = input("Enter your achieved points for the test: ")
    if not testInp.isdigit():
        print("Input Error. Please enter a valid integer between 0 and 20! ")
    elif testInp.isdigit():
        if 0 <= int(testInp) <= 20:
            break
        else:
            print("Input Error. Please enter a valid integer between 0 and 20! ")

# The same for the prüfung
while True:
    examInp = input("Enter your achieved points for the prüfung: ")
    if not examInp.isdigit():
        print("Input Error. Please enter a valid integer between 0 and 70! ")
    elif examInp.isdigit():
        if 0 <= int(examInp) <= 70:
            break
        else:
            print("Input Error. Please enter a valid integer between 0 and 70! ")

# Asks the user if they attended the mündliche präsentation and only breaks the loop if the valid input is made
while True:
    presYesNo = input("Did you attend the mündliche präsentation? ")
    if presYesNo == "yes":
        break
    elif presYesNo == "no":
        print("The mündliche präsentation is MANDATORY ")
    else:
        print("Input Error. Please enter either 'yes' or 'no' ")

# Asks for the achieved points again, this time at the mündliche präsentation, same condition to break the loop
while True:
    presInp = input("Enter your achieved points for the mündliche präsentation: ")
    if not presInp.isdigit():
        print("Input Error. Please enter a valid integer between 0 and 10! ")
    elif presInp.isdigit():
        if 0 <= int(presInp) <= 10:
            break
        else:
            print("Input Error. Please enter a valid integer between 0 and 10! ")

# The if...elif construct to add all points together, check in which range
# the sum of points falls and then prints the corresponding grades to console
print("Out of 100 possible points you scored: " + str(int(testInp) + int(examInp) + int(presInp)))
if 0 <= (int(testInp) + int(examInp) + int(presInp)) < 50:
    print("Based on your input your grade will be: Nicht Genügend (5) ")
elif 50 <= (int(testInp) + int(examInp) + int(presInp)) < 65:
    print("Based on your input your grade will be: Genügend (4) ")
elif 65 <= (int(testInp) + int(examInp) + int(presInp)) < 80:
    print("Based on your input your grade will be: Befriedigend (3) ")
elif 80 <= (int(testInp) + int(examInp) + int(presInp)) < 90:
    print("Based on your input your grade will be: Gut (2) ")
elif 90 <= (int(testInp) + int(examInp) + int(presInp)) <= 100:
    print("Based on your input your grade will be: Sehr Gut (1) ")
else:
    print("Unknown Error")