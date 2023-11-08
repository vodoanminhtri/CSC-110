# Minh Tri Doan Vo
# Match Making logic

# Global constants for over weight toward matching
ATHLETIC_WEIGHT      = 0.15
FOOD_WEIGHT          = 0.10
ENTERTAINMENT_WEIGHT = 0.15
RELATIONSHIP_WEIGHT  = 0.20
RELIGION_WEIGHT      = 0.20
POLITIC_WEIGHT       = 0.20

# Normal rating for all categories
def rate(rating1, rating2):
    rateDifference = rating1 - rating2
    if rateDifference >= 7:
        return 0.0
    elif rateDifference >= 4:
        return 0.4
    elif rateDifference >= 2:
        return 0.7
    elif rating1[4] >= 8 or rating2[4] >= 8:
        if rating1[5] == rating2[5]:
            return 1.0
        else:
            return 0.5
    else:
        return 1.0

# Matching percentage
def match(per1, per2):
    percent = 0.0
    for matchPercent1 in per1:
        for matchPercent2 in per2:
            matchPercent = rate(matchPercent1, matchPercent2)
            percent += matchPercent
            totalPer = percent/6
        print(totalPer)

person1 = (7, 10, 8,  9, 10, "buddism", 6, 8)
person2 = (0,  5, 6, 10,  8, "judaism", 3, 2)
match(person1, person2)