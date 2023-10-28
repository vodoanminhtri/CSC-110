# Minh Tri Doan Vo
# 10/25/2023
# Math library formulas for calculation

import math

def calcDistance(x1, y1, x2, y2):
    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return distance

def calcMidPoint(x1, y1, x2, y2):
    xMidpoint = (x1 + x2) / 2
    yMidpoint = (y1 + y2) / 2
    return xMidpoint, yMidpoint

def calcRadius(x1, y1, x2, y2):
    radius = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return radius