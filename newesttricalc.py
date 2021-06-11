#THIS PROGRAM PERFORMS CALCULATIONS INVOVLING TRIANGLES


#DEFINING FUNCTIONS

#main menu function explaining which values correspond to each option and getting input from the KB
def mainMenu():
    calc = str(input("enter 1 for missing angle calculation, 2 for hypotenuse calculation, 3 to calculate the area of a right angled triangle or q to quit: "))
    return

#Function that calculates the misisng angle of a triangle given two known angles
def missingAngle():
    firstAngle = float(input("enter the first known angle in degrees: "))
    secondAngle = float(input("enter the second known angle in degrees: "))
    sumOfKnown = firstAngle + secondAngle
    ans = 180 - sumOfKnown
    print("the missing angle in degrees = ", ans, "the first known angle in degrees = ", firstAngle, "the second known angle in degrees = ", secondAngle)
    return

#Function that calculates the hypotensue of a triangle given adjacent and opposite side
def hypotenuse():
    adjacent = float(input("enter the length of the adjacent side in cm: "))
    opposite = float(input("enter the length of the opposite side in cm:  "))
    sumOfEachSideSquared = (adjacent**adjacent) + (opposite**opposite)
    ans = sumOfEachSideSquared ** 1/2
    print("hypotensue of the triangle in cm = ", ans, "adjacent side in cm  = ", adjacent, "opposite side in cm = ", opposite)
    return

#Function that calculates the area of a right angled triangle 
def area():
    adjacent = float(input("enter the length of the adjacent side in cm: "))
    opposite = float(input("enter the length of the opposite side in cm: "))
    ans = adjacent*opposite*1/2
    print("area of the triangle in cm squared = ", ans, "adjacent side in cm = ", adjacent, "opposite side in cm = ", opposite)
    return

#Getting input from KB
calc = (input("enter 1 for missing angle calculation, 2 for hypotenuse calculation, 3 to calculate the area of a right angled triangle or q to quit: "))

#while loop that executes if an only if calc is numeric
while(calc.isnumeric()):
   


#While loop that is executed if and only if the user enters 1 at main menu
    while(calc == "1"):
        missingAngle()
        calc = (input("enter 1 for missing angle calculation, 2 for hypotenuse calculation, 3 to calculate the area of a right angled triangle or q to quit: "))
        break
       
    

#While loop that is executed if and only if the user enters 2 at main menu
    while(calc == "2"):
        hypotenuse()
        calc = (input("enter 1 for missing angle calculation, 2 for hypotenuse calculation, 3 to calculate the area of a right angled triangle or q to quit: "))
        break
       
    

#While loop that is executed if and only if the user enters 3 at main menu
    while(calc == "3"):
        area()
        calc = (input("enter 1 for missing angle calculation, 2 for hypotenuse calculation, 3 to calculate the area of a right angled triangle or q to quit: "))
        break
        

#While loop that is executed if an only if the user enters q at the main menu
if(calc == "q"):
    print("Goodbye!")
    quit()
