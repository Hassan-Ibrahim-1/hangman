import os
import random
import time

lives = 6
clear = lambda: os.system('clear') # os.system("clear") for linux   os.system("cls") for windows
gameOver = False
clear()

with open ('hangmanWords',  'r') as file:
    allWords = file.read()
    words = list(map(str, allWords.split()))
    randWord = random.choice(words)
    randWord = randWord.lower()    
    wordLength = len(randWord)

guessedLetters = 0
underScores = []
listRandWords = []
inWord = False
notInWord = False

for x in randWord:
    listRandWords.append(x)

for x in range(wordLength):
    underScores.append("_ ")

wordLengthDisplay = "".join(underScores)

print(wordLengthDisplay)


while gameOver == False:
    print("You have", lives, "lives remaining     Input a letter: ", end="")
    inputLetter = input()
    inputLetter = inputLetter.strip()

    notInWord = False

    if inputLetter.isdigit():
        print("Value entered is not a letter")
        time.sleep(0.5)
        clear()
        print(wordLengthDisplay)
        continue

    for wordIndex in range(len(listRandWords)):
        if listRandWords[wordIndex] == inputLetter:
            inWord = True
            underScores[wordIndex] = inputLetter
            wordLengthDisplay = "".join(underScores)
            clear()
            print(wordLengthDisplay)
            guessedLetters += 1
            continue
            
        elif listRandWords[wordIndex] != inputLetter and inWord == False:
            notInWord = True
            inWord = True

    if notInWord == True:
        lives -= 1
        print("test")
        clear()
        print(wordLengthDisplay)
        notInWord = False
        inWord = True
        
    if lives == 0:
        clear()
        print("You Lost!")
        gameOver = True

    if guessedLetters == wordLength:
        clear()
        print("You Guessed The Word!")
        gameOver = True
            
    clear()
    print(wordLengthDisplay)
