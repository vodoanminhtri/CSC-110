import formulas

BANNER_WIDTH = 50

def main():
    printBanner(1)
    dist = doDistancePractice()
    print("Distance =", dist)
    print()
    printBanner(3)
    x, y = doMidpointPractice()
    print("Midpoint x = ", x)
    print("Midpoint y = ", y)
    print()
    printBanner(0)
    dista = doRadiusPractice()
    print("Radius =", dista)

def printBanner(x):
    if x == 1:
        print("-" * BANNER_WIDTH)
        print("\tDISTANCE PRACTICE")
        print("-" * BANNER_WIDTH)
    elif x == 3:
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
    inputX1, inputY1, inputX2, inputY2 = userInputDistance()
    caldistance = formulas.calcDistance(inputX1, inputY1, inputX2, inputY2)
    return caldistance

def doMidpointPractice():
    midPx1, midPy1, midPx2, midPy2 = userInputMidpoint()
    midPointX = formulas.calcMidPointX(midPx1, midPy1, midPx2, midPy2)
    midPointY = formulas.calcMidPointY(midPx1, midPy1, midPx2, midPy2)
    return midPointX, midPointY

def doRadiusPractice():
    cenX, cenY, ptX, ptY = userInputRadius()
    radius = formulas.calcRadius(cenX, cenY, ptX, ptY)
    return radius

main()
