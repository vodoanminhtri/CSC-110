# Minh Tri Doan Vo
# 10/25/2023
# Calculation of Distance, Mid Point, and Radius from User Input
import formulas
BANNER_WIDTH = 50

def main():
    doDistancePractice()
    print()
    doMidpointPractice()
    print()
    doRadiusPractice()
    print()
    print("That wraps up practice time. See you next time!")

def printBanner(x):
    if x == 1:
        print("-" * BANNER_WIDTH)
        print("\tDISTANCE PRACTICE")
        print("-" * BANNER_WIDTH)
    elif x == 2:
        print("-" * BANNER_WIDTH)
        print("\tMIDPOINT PRACTICE")
        print("-" * BANNER_WIDTH)       
    else:
        print("-" * BANNER_WIDTH)
        print("\tRADIUS PRACTICE")
        print("-" * BANNER_WIDTH)
        
def userInputDistance():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    return x1, y1, x2, y2

def userInputMidpoint():
    midX1 = float(input("Enter x1: "))
    midY1 = float(input("Enter y1: "))
    midX2 = float(input("Enter x2: "))
    midY2 = float(input("Enter y2: "))
    return midX1, midY1, midX2, midY2

def userInputRadius():
    centerX = float(input("Enter center x: "))
    centerY = float(input("Enter center y: "))
    pointX = float(input("Enter point x: "))
    pointY = float(input("Enter point y: "))
    return centerX, centerY, pointX, pointY

def doDistancePractice():
    printBanner(1)
    inputX1, inputY1, inputX2, inputY2 = userInputDistance()
    caldistance = formulas.calcDistance(inputX1, inputY1, inputX2, inputY2)
    print("Distance =", format(caldistance, ".4f"))
    return caldistance

def doMidpointPractice():
    printBanner(2)
    midPx1, midPy1, midPx2, midPy2 = userInputMidpoint()
    midPointX, midPointY = formulas.calcMidPoint(midPx1, midPy1, midPx2, midPy2)
    print("Midpoint x = ", format(midPointX, ".4f"))
    print("Midpoint y = ", format(midPointY, ".4f"))
    return midPointX, midPointY

def doRadiusPractice():
    printBanner(0)
    cenX, cenY, ptX, ptY = userInputRadius()
    radius = formulas.calcRadius(cenX, cenY, ptX, ptY)
    print("Radius =", format(radius, ".4f"))
    return radius

main()
