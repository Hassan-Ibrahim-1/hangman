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
listRandWord = []
listGuessedLetters = []
notInWord = False
alreadyGuessed = False
guessedLettersDisplay = set()

for x in randWord:
    listRandWord.append(x)

for x in range(wordLength):
    underScores.append("_ ")

wordLengthDisplay = "".join(underScores)

print(wordLengthDisplay)


while gameOver == False:
    if guessedLettersDisplay == set():
        pass
    else:
        print("Guessed Letters:", guessedLettersDisplay)
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

    for wordIndex in range(len(listRandWord)):
        if listRandWord[wordIndex] == inputLetter:
            notInWord = True
            underScores[wordIndex] = inputLetter
            wordLengthDisplay = "".join(underScores)
            clear()
            print(wordLengthDisplay)
            guessedLetters += 1
        else:
            pass
    listGuessedLetters.append(inputLetter)
    guessedLettersDisplay.add(inputLetter)
            

    if notInWord == False:
            lives -= 1
            print("\n\nThe letter'", inputLetter, "'is not in the word")
            time.sleep(0.8)
            clear()
            print(wordLengthDisplay)
            notInWord = False
        
    if lives == 0:
        clear()
        print("You Lost! The word was:", randWord)
        gameOver = True

    if guessedLetters == wordLength:
        clear()
        print("You Guessed The Word:", randWord)
        gameOver = True
