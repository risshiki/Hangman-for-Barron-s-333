import random

wordlist = []
worddict = {}


f = open("wordlist.txt",'r')

givenChoice = False

while not givenChoice:
    print("Choose from options below")
    print("1. All words")
    print("2. Revise words that are done")
    print("3. Only new words")
    print("4. Words you don't know")
    print("5. New words you don't know")
    choice = input()
    
    if choice == '1' or choice == '3':
        f = open("wordlist.txt",'r')
        givenChoice = True 
    
    elif choice == '2':
        f = open("revisedwords.txt",'r')
        givenChoice = True
    elif choice == '4' or choice =='5':
        f = open("notlearntwords.txt",'r')
        givenChoice = True
    else:
        print("Please enter a valid option")


for line in f:
    definition = line.split('\t')
    definition[0] = definition[0].lower()
    wordlist.append(definition[0])
    worddict[definition[0]] = definition[1]

wordlist.sort()

words = wordlist



HANGMANPICS = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']


def getRandomWord(wordList):
 # This function returns a random string from the passed list of strings.
 wordIndex = random.randint(0, len(wordList) - 1)
 return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
 print(HANGMANPICS[len(missedLetters)])
 print()

 print('Missed letters:', end=' ')
 for letter in missedLetters:
     print(letter, end=' ')
 print()

 blanks = '_' * len(secretWord)

 for i in range(len(secretWord)): # replace blanks with correctly guessed letters
     if secretWord[i] in correctLetters:
         blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

 for letter in blanks: # show the secret word with spaces in between each letter
     print(letter, end=' ')
 print()

def getGuess(alreadyGuessed):
 # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
 while True:
     print('Guess a letter.')
     guess = input()
     guess = guess.lower()
     if len(guess) != 1:
         print('Please enter a single letter.')
     elif guess in alreadyGuessed:
         print('You have already guessed that letter. Choose again.')
     elif guess not in 'abcdefghijklmnopqrstuvwxyz':
         print('Please enter a LETTER.')
     else:
         return guess

def playAgain():
 # This function returns True if the player wants to play again, otherwise it returns False.
 print('Do you want to play again? (yes or no)')
 return input().lower().startswith('y')

def ifWordRevised(secretWord):
    print("Checking if word revised")
    checkline = secretWord + "\t" + worddict[secretWord]
    r = open("revisedwords.txt",'r')
    for line in r:
         if checkline in line:
             return True
    return False
    
print('\n\nH A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
usedWordFlag = True
#Will only be used in checking for new words

if choice == '3' or choice =='5':
    counter = 0
    while usedWordFlag:
        secretWord = getRandomWord(words)
        usedWordFlag = ifWordRevised(secretWord)
        counter += 1

        if counter == 100:
            usedWordFlag = False

for letter in secretWord:
    if letter in "aeiou":
        correctLetters = correctLetters + letter
gameIsDone = False

while True:
 displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
 print("Definition : " + worddict[secretWord]) 
 # Let the player type in a letter.
 guess = getGuess(missedLetters + correctLetters)

 if guess in secretWord:
     correctLetters = correctLetters + guess

     # Check if the player has won
     foundAllLetters = True
     for i in range(len(secretWord)):
         if secretWord[i] not in correctLetters:
             foundAllLetters = False
             break
     if foundAllLetters:
         print('Yes! The secret word is "' + secretWord + '"! You have won!')
         gameIsDone = True
 else:
     missedLetters = missedLetters + guess

     # Check if player has guessed too many times and lost
     if len(missedLetters) == len(HANGMANPICS) - 1:
         displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
         print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
         gameIsDone = True

 # Ask the player if they want to play again (but only if the game is done).
 if gameIsDone:

     appendline = secretWord + "\t" + worddict[secretWord] 
     r = open("revisedwords.txt",'r')
     flag = True
     for line in r:
         if appendline in line:
             flag = False
             break
     r.close()
     if flag:    
         with open("revisedwords.txt",'a') as f:
             f.write(appendline)
         f.close()
    
     if playAgain():
         missedLetters = ''
         correctLetters = ''
         gameIsDone = False
         secretWord = getRandomWord(words)
         for letter in secretWord:
            if letter in "aeiou":
                correctLetters = correctLetters + letter
     else:
         break