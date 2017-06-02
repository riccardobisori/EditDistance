from Ngrams import Ngrams

ngrams = Ngrams()


# generateFileBigram() e generateFileTriGram() vanno eseguite solo una volta, all'inizio, per generare i file di n-gram
# che contengono le parole del lessico corrispondenti


def generateFileBiGram():
    alphabet = __import__("string").lowercase  # restituisce l'alfabeto minuscolo

    for i in alphabet:
        for j in alphabet:
            nomeFile = 'file-' + i + j + '.txt'
            open(nomeFile, "w")

    nomi = open("NomiPropri.txt", "r")

    for k in nomi:
        name = k[:len(k) - 1]  # elimino il carattere \n alla fine della parola
        gram = ngrams.biGram(name)

        for i in gram:
            fileName = 'file-' + i + '.txt'
            f = open(fileName, "a")
            f.write(name + "\n")


def generateFileTriGram():
    alphabet = __import__("string").lowercase

    for firstLetter in alphabet:
        for secondLetter in alphabet:
            for thirdLetter in alphabet:
                nomeFile = 'file-' + firstLetter + secondLetter + thirdLetter + '.txt'
                open(nomeFile, "w")

    nomi = open("NomiPropri.txt", "r")

    for k in nomi:
        name = k[:len(k) - 1]
        gram = ngrams.triGram(name)

        for i in gram:
            fileName = 'file-' + i + '.txt'
            f = open(fileName, "a")
            f.write(name + "\n")

# generateFileBiGram()
# generateFileTriGram()
