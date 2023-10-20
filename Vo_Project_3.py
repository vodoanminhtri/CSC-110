# Minh Tri Doan Vo
# Create a banner header to format output display

# declared global variables
FULL_NAME   = ""
DATE        = ""
PROG_NAME   = ""
DESCRIPT    = ""
# constant for how many stars will display in displayStarLine()
STAR_LINE   = 80

# use global to bring in the global variable from above
def collectInputs():
    global FULL_NAME, DATE, PROG_NAME, DESCRIPT
    FULL_NAME   = input("Enter your name: ")
    DATE        = input("Date: ")
    PROG_NAME   = input("Program: ")
    DESCRIPT    = input("Description: ")

# print user the variable instead of calling for the function
def displayBanner():
    displayStarLine()
    print("\tCoder\t:", FULL_NAME)
    print("\tDate\t:", DATE)
    print("\tProgram\t:", PROG_NAME)
    print("\tDescrip\t:", DESCRIPT)
    displayStarLine()

def displayStarLine():
    print("*" * STAR_LINE)

def displaySectHeaders():
    print()
    displaySectHeader("\tConstants")
    print()
    displaySectHeader("\tVariables")
    print()
    displaySectHeader("\tInput")
    print()
    displaySectHeader("\tProcessing")
    print()
    displaySectHeader("\tOutput")

def displaySectHeader(sectionName):
    displayStarLine()
    print(sectionName)
    displayStarLine()

def main():
    print()
    collectInputs()
    displayBanner()
    displaySectHeaders()

main()
