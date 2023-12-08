def readFile(textFile):
    originalFile = open(textFile, "r")
    textSet = set(originalFile.read().split())
    originalFile.close()
    return textSet

def findLongest(setOfWord):
    longest = ""
    longestLen = 0
    for word in setOfWord:
        if len(word) > len(longest):
            longest = word
            longestLen = len(longest)
    return longest, longestLen

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
    setOfWords = list(setOfWords)
    frequenciesList = [0] * (longestLen + 1)
    for word in setOfWords:
        wordLength = len(word)
        frequenciesList[wordLength] += 1
    return frequenciesList

def main():
    file = readFile("GettysburgAddress.txt")
    totalDistictWord = len(file)
    longestWord, longestLen = findLongest(file)
    list = generateSortedList(file)
    writeWordFile("GettysburgWords.txt", list)
    frequencies = generateLenFreqs(file, longestLen)

    print("Number of distinct words:", format(totalDistictWord, "3d"))
    print("Length of longest word:", format(longestLen, "5d"))
    print("Longest word:", longestWord)
    print()
    print("Length = 1, Count =", format(frequencies[1], "4d"))
    print("Length = 2, Count =", format(frequencies[2], "4d"))
    print("Length = 3, Count =", format(frequencies[3], "4d"))
    print("Length = 4, Count =", format(frequencies[4], "4d"))
    print("Length = 5, Count =", format(frequencies[5], "4d"))
    print("Length = 6, Count =", format(frequencies[6], "4d"))
    print("Length = 7, Count =", format(frequencies[7], "4d"))
    print("Length = 8, Count =", format(frequencies[8], "4d"))
    print("Length = 9, Count =", format(frequencies[9], "4d"))
    print("Length = 10, Count =", format(frequencies[10], "3d"))
    print("Length = 11, Count =", format(frequencies[11], "3d"))

main()
