# Minh Tri Doan Vo
# CSC 110
# Project 9

def readFile(textFile):
    originalFile = open(textFile, "r")
    textSet = set(originalFile.read().split())
    originalFile.close()
    return textSet

def findLongest(setOfWord):
    longgest = ""
    longgestLen = 0
    for word in setOfWord:
        if len(word) > len(longgest):
            longgest = word
            longgestLen = len(longgest)
    return longgest, longgestLen

def generateSortedList(setOfWord):
    setOfWord = list(setOfWord)
    for passStartIndex in range(len(setOfWord) - 1):
        smallestIndex = passStartIndex
        for checkIndex in range(passStartIndex + 1, len(setOfWord)):
            if setOfWord[checkIndex] < setOfWord[smallestIndex]:
                smallestIndex = checkIndex
        temp = setOfWord[passStartIndex]
        setOfWord[passStartIndex] = setOfWord[smallestIndex]
        setOfWord[smallestIndex] = temp
    return setOfWord

def writeWordFile(writeFile, listOfWords):
    writting = open(writeFile, "w")
    for word in listOfWords:
        writting.write(word + "\n")
    writting.close()

def generateLenFreqs(setOfWords, longestLen):
    pass

def main():
    file = readFile("GettysburgAddress.txt")
    print(len(file))
    long, longger = findLongest(file)
    print(long, longger)
    list = generateSortedList(file)
    print(list)
    writeWordFile("GettysburgWords.txt", list)
    frequencies = generateLenFreqs(file, longger)
    print(frequencies)
    


main()