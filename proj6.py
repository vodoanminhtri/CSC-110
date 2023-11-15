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
    name = getNonEmptyString(name)
    readingLocation = input("Enter Location: ")
    readingLocation = getNonEmptyString(readingLocation)
    print()
    result = []
    # logic for the loop
    month = int(input("Enter month (or 0 to exit): "))
    counter = 0
    while month != 0:
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
    average = sum(result)/counter
    return name, readingLocation, smallestValue, biggestValue, average, counter

def main():
    nameInput, locationInput, minLevel, maxLevel, averageLevel, count = enterCo2ReadingBatch()
    print("-" * 50)
    print("Recorder Name:\t\t", nameInput)
    print("Reading location:\t", locationInput)
    print()
    print("Number of readings:", format(count, "7.0f"))
    print("Minimum CO2 Level:", format(minLevel, "8.0f"))
    print("Maximum CO2 Level:", format(maxLevel, "8.0f"))
    print("Average CO2 Level:", format(averageLevel, "8.0f"))
    print("-" * 50)

main()
