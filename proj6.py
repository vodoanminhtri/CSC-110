# Minh Tri Doan Vo
# 11/15/2023
# CO2 Data Entry and Stats, Data validation

def getNonEmptyString(validString):
    while len(validString) == 0:
        validString = input("ERROR: Please enter valid data: ")
    return validString

def getInRangeInteger(min, max, validInt):
    while validInt < min or validInt > max:
        validInt = int(input("ERROR Enter a valid data: "))
    return validInt

def enterCo2ReadingBatch():
    # user input
    name = input("Enter Name: ")
    name += getNonEmptyString(name)
    readingLocation = input("Enter Location: ")
    readingLocation += getNonEmptyString(readingLocation)
    print()
    result = []
    # logic for the loop
    month = int(input("Enter month (or 0 to exit): "))
    while month > 0:
        counter = 1
        month = getInRangeInteger(1, 12, month)
        day = int(input("Enter day: "))
        day = getInRangeInteger(1, 31, day)
        year = int(input("Enter year: "))
        year = getInRangeInteger ( 2022, 2099, year)
        co2Reading = int(input("Enter CO2 Reading: "))
        co2Reading = getInRangeInteger(1, 10000, co2Reading)
        counter += 1
        print()
        month = int(input("Enter month (or 0 to exit): "))  
        result.append(co2Reading)  
    # calculation for min
    smallestValue = min(result)
    biggestValue = max(result)
    average = (smallestValue + biggestValue)/2
    return name, readingLocation, smallestValue, biggestValue, average, counter

def main():
    name, location, minLevel, maxLevel, averageLevel, count = enterCo2ReadingBatch()
    print("-" * 30)
    print("Recorder Name:", name)
    print("Reading location:", location)
    print()
    print("Number of readings:", count)
    print("Minimum CO2 Level:", minLevel)
    print("Maximum CO2 Level:", maxLevel)
    print("Average CO2 Level:", averageLevel)
    print("-" * 30)

main()
