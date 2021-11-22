import os
import random

Lives = 6
clear = lambda: os.system('clear') # os.system("clear") for linux   os.system("cls") for windows
gameOver = False

with open ('hangmanWords',  'r') as file:
    allWords = file.read()
    words = list(map(str, allWords.split()))
    randWord = random.choice(words)
    randWord = randWord.lower()    
    wordLength = len(randWord)

underScores = []
listRandWords = []

for x in randWord:
    listRandWords.append(x)


for x in range(wordLength):
    underScores.append("_ ")

wordLengthDisplay = "".join(underScores)

print(wordLengthDisplay)


while gameOver == False:
    inputLetter = input("Input a Letter: ")
    for wordIndex in range(len(listRandWords)):
        if listRandWords[wordIndex] == inputLetter:
            underScores[wordIndex] = inputLetter
            wordLengthDisplay = "".join(underScores)

            
    clear()
    print(wordLengthDisplay)
