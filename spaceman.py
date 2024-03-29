import random #library that has shuffle, random, choice, etc.

def load_word(): #function to load word
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r') # opens file
    words_list = f.readlines()  # readlines means everything inside of file
    f.close() # closes path

    words_list = words_list[0].split(' ') # split words in word file by characters
    secret_word = random.choice(words_list) # selecting split from word list
    return(secret_word) #secret word returned




def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

    lengthofsecretword = len(secret_word)
    i = 0

    for letter in letters_guessed:
        number_of_letters = secret_word.count(letter)
        print(number_of_letters)
        if (number_of_letters > 0):
            i += number_of_letters

    if lengthofsecretword == i:
        return True
    else:
        return False

        #pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    wordsstring = ""
    #TODO: Loop through the letters in secret word and build a string that shows
    #the letters that have been guessed correctly so far that are saved in letters_guessed and underscores
    #for the letters that have not been guessed yet

    for letters in secret_word: #creating letter variables and putting secret_word in it
        if letters in letters_guessed: #if any letters are in that word
            wordsstring += (letters + ' ') #assigning word character to word string variable
        else:
            wordsstring += "_ "
    return wordsstring



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''

    for letter in secret_word:
        if guess == letter:
            return True
    return False

    #TODO: check if the letter guess is in the secret word

    #pass


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    #TODO: show the player information about the game according to the project spec

    print('\n\nWelcome To Spaceman')
    print(secret_word)

    letters_guessed = []
    attempts = 7
    running = True

    while (is_word_guessed(secret_word, letters_guessed) == False and attempts > 0):
        '''
        if attempts < 1:
            print ('too low')
            running = False
            return
        '''
        print('You have ' + str(attempts) + ' attempts remaining')
        get_guessed_word(secret_word, letters_guessed)
        guess = input("Guess the character ")
        '''
        if is_word_guessed(secret_word, letters_guessed) == False:
            print('coooo')
        else:
            running = False
            return
        '''


        if not (guess.isalpha() == True and len(guess) == 1):
            print('Try again. Input one letter only from the alphabet.')
        elif (guess in letters_guessed):
            print ('you already used that letter')
        else:
            letters_guessed += guess
            if is_guess_in_word(guess, secret_word) == True:
                print('Nice!')
                    #get_guessed_word(secret_word, letters_guessed)
            else:
                attempts -= 1
                print('The letter is not in the word')


    if (attempts < 1):
        print ("You're out of attempts. lose.")

    else:
        print ('You win. ')
            #index = secret_word.find(guess) #  finds index of guess in secret word
            #print(index)


    #print(letters_guessed)



    #TODO: Ask the player to guess one letter per round and check that it is only one letter



    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost





if __name__ == '__main__':
    #These function calls that will start the game
    secret_word = load_word()
    spaceman(secret_word)
