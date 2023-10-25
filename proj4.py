import formulas

BANNER_WIDTH = 50

def printBanner():
    pass

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
    pass

def main():
    print("Distance =", doDistancePractice())
    print()
    print("Midpoint x = ", doMidpointPractice()[0])
    doRadiusPractice()

main()
