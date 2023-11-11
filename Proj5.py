# Global constants for overall weight toward matching
ATHLETIC_WEIGHT      = 0.15
FOOD_WEIGHT          = 0.10
ENTERTAINMENT_WEIGHT = 0.15
RELATIONSHIP_WEIGHT  = 0.20
RELIGION_WEIGHT      = 0.20
POLITIC_WEIGHT       = 0.20

# Normal rating for all categories
def rate(rating1, rating2):
    rateDifference = abs(rating1 - rating2)
    if rateDifference >= 7:
        return 0.0
    elif rateDifference >= 4:
        return 0.4
    elif rateDifference >= 2:
        return 0.7
    else:
        return 1.0

# Matching percentage
def match(per1, per2):
    athletic      = rate(per1[0], per2[0])
    food          = rate(per1[1], per2[1])
    entertainment = rate(per1[2], per2[2])
    relationship  = rate(per1[3], per2[3])
    religion      = rate(per1[4], per2[4])
# Logic for religion
    if per1[4] >= 8 or per2[4] >= 8:
        if per1[5] == per2[5]:
            religion = 1.0
        else:
            religion = 0.50
    else:
        religion = rate(per1[4], per2[4])
# Logic for political
    if per1[6] >= 9 or per2[6] >= 9:
        political = rate(per1[7], per2[7])
    else:
        political = rate(per1[6], per2[6])
# Total match percentage
    totalMatch = (athletic * ATHLETIC_WEIGHT +
                  food * FOOD_WEIGHT +
                  entertainment * ENTERTAINMENT_WEIGHT +
                  relationship * RELATIONSHIP_WEIGHT +
                  religion * RELIGION_WEIGHT +
                  political * POLITIC_WEIGHT)
    return totalMatch*100

def main():
# atheltic = a, foodOut = f, entertainmentOut = e, seriousRelationship = s
# religious = r, religion = specific religion
# politics = p, political leaning = l
#              a   f  e   s   r   religion  p  l
    person1 = (7, 10, 8,  9, 10, "buddism", 6, 8)
    person2 = (4,  5, 6, 10,  8, "judaism", 3, 2)
    print("Overall is sum of weighted contributions:", str(format(match(person1, person2), ".0f")) + "%")

main()
