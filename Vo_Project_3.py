# Minh Tri Doan Vo
# Create a banner header to format output display

fullName    = input("Enter your name: ")
date        = input("Date: ")
progName    = input("Program: ")
descript    = input("Description: ")
# constant for how many stars will display in displayStarLine()
starLine    = 80

def collectInputs():
    print("\tCoder\t:", fullName)
    print("\tDate\t:", date)
    print("\tProgram\t:", progName)
    print("\tDescrip\t:", descript)

def displayBanner():
    displayStarLine()
    collectInputs()
    displayStarLine()

def displayStarLine():
    print("*" * starLine)

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
    displayBanner()
    displaySectHeaders()

main()

# Summary Report
# I couldn't figure out how to get the input inside the collectInputs() to be a global variables
# so I did the next best solution I could think of. By making the global variable and then call
# for it at the collectInputs(). I moved def main() to the bottom because it make more sense
# to me that way. I know my main() didn't call the collectInputs(). However, when I tried
# to call the collectInputs() inside of main, the output would display twice. So I opted to
# not call for it in main but inside the displayBanner().