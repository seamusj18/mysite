import os
import random as rand
import time
os.system('cls')

wordSet = ["cat", "dog", "expert", "cup", "house", "camel", "cello", "school", "lesson", "teach"]
countdownNums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def question(questionAsked, validAnswers):
    answerValid = False
    while(answerValid == False):
        userInput = input(questionAsked)
        userInput = userInput.lower()
        userInput = userInput.replace(" ", "")
        if(userInput in validAnswers):
            answerValid = True
            return userInput
        else:
            os.system('cls')
            print("Invalid Answer.")
def hmGraphic(stage):
    if(stage == 0):
        print("  __________")
        print("  |        |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("__|__")
    elif(stage == 1):
        print("  __________")
        print("  |        |")
        print("  |        o")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("__|__")
    elif(stage == 2):
        print("  __________")
        print("  |        |")
        print("  |        o")
        print("  |        |")
        print("  |")
        print("  |")
        print("  |")
        print("__|__")
    elif(stage == 3):
        print("  __________")
        print("  |        |")
        print("  |        o")
        print("  |        |")
        print("  |       / ")
        print("  |")
        print("  |")
        print("__|__")
    elif(stage == 4):
        print("  __________")
        print("  |        |")
        print("  |        o")
        print("  |        |")
        print("  |       / \\")
        print("  |")
        print("  |")
        print("__|__")
    elif(stage == 5):
        print("  __________")
        print("  |        |")
        print("  |        o")
        print("  |        |\\")
        print("  |       / \\")
        print("  |")
        print("  |")
        print("__|__")
    elif(stage == 6):
        print("  __________")
        print("  |        |")
        print("  |        o")
        print("  |       /|\\")
        print("  |       / \\")
        print("  |")
        print("  |")
        print("__|__")

while True:
    wordValid = False
    containsSpaces = True
    wordDisplayedList = []
    lettersGuessed = []
    solved = False
    os.system('cls')
    x = 0
    incorrectGuesses = 0
    guessValid = False
    correctGuess = False

    wordChoiceQuestion = "Would you like to give the program a specific word to use, or have it supply one for you? Enter 'E' if you want to enter a word, and 'S' If you would like the program to supply one for you. "
    wordChoiceValidAns = ["e", "s"]
    wordChoice = question(wordChoiceQuestion, wordChoiceValidAns)
    os.system('cls')

    while(wordValid == False or containsSpaces == True):

        if(wordChoice == "e"):
            word = input("What word you you like to be used? (Letters only)  ")
        if(wordChoice == "s"):
            pfaiwpiagiopa = len(wordSet) - 1
            word = wordSet[rand.randint(0, pfaiwpiagiopa)]
        word = word.lower()
        if(' ' not in word):
            containsSpaces = False
        wordList = word.replace("", " ")
        wordList = wordList.split()
        wordValid = True
        for x in wordList:
            if(x in letters):
                os.system('cls')
            else:
                wordValid = False
                

    wordLength = len(wordList)
    
    #get the list that will be shown to the user
    x = 0
    while(x < wordLength):
        wordDisplayedList.insert(x, "_")
        x = x+1
    x = 0
        


    #Mock loading screen because why not lmao
    os.system('cls')
    print("Starting game.")
    time.sleep(3)

    os.system('cls')

    guess = ''
    #Start of the game
    while(incorrectGuesses < 6 and solved == False):
        x = 0
        while(guessValid == False):
            os.system('cls')
            guessValid = False
            wordDisplayed = "  ".join(wordDisplayedList)
            hmGraphic(incorrectGuesses)
            print(wordDisplayed)
            print('Incorrect guesses: ' + ' '.join(lettersGuessed))
            if(x > 0):
                print('Invalid Guess.')
            guess = input("What letter would you like to guess?  ")
            guess = guess.lower()
            if(len(guess) == 1):
                guessValid = True
            if(guess in letters):
                guessValid = True
            elif(guess not in letters):
                guessValid = False
            x = x + 1
        if(guess in wordList):
            y = 0
            for x in wordList:
                if(guess == wordList[y]):
                    wordDisplayedList[y] = guess.upper()
                y = y + 1
            y = 0
        elif(guess not in wordList):
            if(guess.upper() not in lettersGuessed):
                incorrectGuesses = incorrectGuesses + 1
                lettersGuessed.append(guess.upper())
        guessValid = False
        if('_' not in wordDisplayedList):
            solved = True

        
    wordDisplayed = " ".join(wordDisplayedList).upper()
        

    if(solved == False):
        for x in range (10):
            os.system('cls')
            hmGraphic(incorrectGuesses)
            print(wordDisplayed)
            print('Incorrect guesses: ' + ' '.join(lettersGuessed))
            print("Game failed. Restarting in " + str(countdownNums[x]) + " seconds.")
            print("The word was: " + word.upper())
            time.sleep(1)
    elif(solved == True):
        for x in range (10):
            os.system('cls')
            hmGraphic(incorrectGuesses)
            print(wordDisplayed)
            print('Incorrect guesses: ' + ' '.join(lettersGuessed))
            print("You win! Restarting in " + str(countdownNums[x]) + " seconds.")
            time.sleep(1)