from datetime import datetime as dt
import signal
import sys
from threading import Timer

random_word = "books" #word to guess
remaining_time = 30 #timer from game onset
blank = ["_"] * len(random_word) #display
max_tries = 5 #maximum number of tries
incorrect_guesses = 0 #initialize incorrect guesses

while True: 
    t = Timer(remaining_time, print, ["Time's up! Press any key to continue."]) #appears when time limit is up
    t.start()
    word = "" #initialize guessed letters
    remaining_tries = max_tries - incorrect_guesses #get number of remaining guesses
    print("\nRemaining guesses: {}".format(remaining_tries))
    for c in blank: #letter library
        word = word + "{} ".format(c)

    print(word.upper()) #displays correct guess letters in uppercase
    if "_" not in blank: #terminates if no more _ on display
        t.cancel() #cancel timer
        sys.exit("Good job! You're safe!") #exits game

    start_time = dt.now()
    answer = str(input("\nGuess a letter: ")) #input

    if not t.is_alive(): #checks if timer is terminated
        sys.exit("Exiting..")

    if len(answer) == 1: #check if 1 letter is entered
        if answer.lower() in random_word.lower(): #checks if letter matches a letter in word to guess
            match = True #if it matches, continue
            for idx, letter in enumerate(random_word): #loop for checking correct guesses
                if answer.lower() == letter.lower(): #matching letters from guess to word to guess
                    blank[idx] = answer #put correct guess on display
        else:
            match = False #returns to loop; input guess
    else:
        print("Please input one letter [a-z] only!") #if >1 is entered

    if not match:
        incorrect_guesses+=1

    if incorrect_guesses == max_tries:
        t.cancel()
        sys.exit("Sorry! Say hi to San Pedro for me!")

    end_time = dt.now()
    elapsed_time = end_time - start_time
    t.cancel()

    remaining_time = remaining_time - elapsed_time.seconds
