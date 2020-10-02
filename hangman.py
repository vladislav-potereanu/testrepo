import time
import random
name = input("What is your name? ")
print ("Hello, " + name, "Time to play hangman!")
print ("")
#wait for 1 second
time.sleep(1)
print ("Start guessing...")
time.sleep(0.5)
word = random.choice(["secret", "avengers", "superman", "batman", "hulk", "antman", "spiderman", "flash"])
#creates an variable with an empty value
guesses = ''
#determine the number of turns
turns = 10
#check if the turns are more than zero
while turns > 0:
    failed = 0
    # for every character in secret_word
    for char in word:
    # see if the character is in the players guess
        if char in guesses:
            print (char)
        else:
        # if not found, print a dash
            print ("_")
       # and increase the failed counter with one
            failed += 1
    # if failed is equal to zero
    # print You Won
    if failed == 0:
        print ("You won")
    # exit the script
        break
    # ask the user go guess a character
    guess = input("guess a character: ")
    # set the players guess to guesses
    guesses += guess
    # if the guess is not found in the secret word
    if guess not in word:
        turns -= 1
        print ("Wrong")

    # how many turns are left
        print ("You have", + turns, 'more guesses')

    # if the turns are equal to zero
        if turns == 0:
            # print "You Lose"
            print ("You Lose")
