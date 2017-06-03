from EditDistance import editDistance
from Ngrams import Ngrams
from timeit import default_timer as timer

ngrams = Ngrams()


def testEditDistance():
    query = raw_input("Enter a name to search for: ")
    lengthEdit = input("Enter Edit_Distance reference value (max distance): ")

    nomi = open("NomiPropri.txt", "r")
    namesFound = []
    query += "\n"
    start = timer()
    for i in nomi:
        edit = editDistance(query, i)
        if edit <= lengthEdit:
            namesFound.append(i)
    end = timer()

    if len(namesFound) == 0:
        print "No names found."

    else:
        print "Maybe you were searching for: ",
        for i in namesFound:
            names = i[:len(i) - 1]
            print names,

    print " "
    print "\nEdit_Distance time: ", end - start
    print


def testNGram():
    query = raw_input("Enter a name to search for: ")

    n = input("Enter n-gram size (only 2 or 3): ")

    while (n is not 2) and (n is not 3):
        n = input("Error.\nEnter n-gram size (only 2 or 3): ")
    lengthEdit = input("Enter Edit_Distance reference value (max distance): ")

    namesFound = []

    start = timer()
    if n == 2:
        nGramQuery = ngrams.biGram(query)
    else:
        nGramQuery = ngrams.triGram(query)

    for i in range(len(nGramQuery)):
        fileName = "NGrams//file-" + nGramQuery[i] + ".txt"

        openFile = open(fileName, "r")
        query += "\n"

        for j in openFile:
            edit = editDistance(query, j)
            if edit <= lengthEdit:
                namesFound.append(j)

    end = timer()

    if len(namesFound) == 0:
        print "No names found."

    else:
        print "\nMaybe you were searching for: ",
        for i in namesFound:
            names = i[:len(i) - 1]
            print names,

    print " "
    print "\nTime with Ngrams: ", end - start


testEditDistance()
testNGram()
