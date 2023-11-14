# Minh Tri Doan Vo
# 11/15/2023
# CO2 Data Entry and Stats, Data validation

def getNonEmptyString(validString):
    while len(validString) == 0:
        print("ERROR: Please enter Your Name")
        validString = input("Enter Your Full Name: ")
    return validString

def getInRangeInteger(min, max, validInt):
    while validInt < min or validInt > max:
        validInt = int(input("ERROR Enter a valid data: "))
    return validInt

def enterCo2ReadingBatch():
    # user input
    name = input("Enter Name: ")
    getNonEmptyString(name)
    readingLocation = input("Enter Location: ")
    getNonEmptyString(readingLocation)
    print()
    # logic for the loop
    month = int(input("Enter month (or 0 to exit): "))
    while month > 0:
        counter = 1
        getInRangeInteger(1, 12, month)
        day = int(input("Enter day: "))
        getInRangeInteger(1, 31, day)
        year = int(input("Enter year: "))
        getInRangeInteger ( 2022, 2099, year)
        co2Reading = int(input("Enter CO2 Reading: "))
        getInRangeInteger(1, 10000, co2Reading)
        counter += 1
        print()
        month = int(input("Enter month (or 0 to exit): "))
    return name, readingLocation, month, day, year, co2Reading, counter

def main():
    data = []
    dataInput = enterCo2ReadingBatch()
    data += dataInput
    print(data)

main()