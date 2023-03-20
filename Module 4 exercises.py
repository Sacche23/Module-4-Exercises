# What is a variable?
#  A variable is a way to store and labeled data in code to be referred to or changed later on. 
# What is a constant?
#  A variable (usually named in all caps) that is not meant to change within a code
# Can a variable be changed once assigned?
#  Yes, for example:

number = 8
print(number)
number += 1
print(number)

# Write a program that counts for the user. Let the user enter the starting number, the ending number, and the amount by which to count.

print('\nHello! This is a counting machine. Please enter the starting value, ending value, and by how much to count each time.\n')

starting = int(input("Starting value: "))

ending = int(input("Ending value: "))

count = int(input("Increment value: "))

print("Counting...beep boop...:")
for values in range(starting, ending, count):
    print(values, end = ' ')
    

# Create a program that gets a message from the user and then prints it out backwards.

word = input('Please enter a message to be typed out backwards: ')
position = -1
newWord = ''

for chars in word:
    newWord += word[position]
    position -= 1

print(newWord)
    
# Create a game where the computer picks a random word and the player has to guess that word. The computer tells the player how many letters are in the word. Then the player gets five chances to ask if a letter is in the word. The computer can only respond with “yes” or “no”. Then, the player must guess the word.

import random

WORDS = ('church', 'serendipity', 'ineffible', 'hater', 'cheese', 'noise', 'accent')

word = random.choice(WORDS)

correct = word

chances = 5

input("Hello! Welcome to Word Guesser (filmed in front of a live studio audience). I will think of a random word and you'll have 5 chances to ask if a specific letter is in the mystery word. After that, you must make your guess. Ready to start? Press enter. \n")

print('The mystery word has', len(word), 'letters in it.\n')

letter = input('What is a letter that you think might be in the mystery word?\n')

if len(letter) > 1:
    while chances > 1:
        print("\nHey! That's more than one letter! I'll take a chance for wasting my time.\n")
        chances -= 1
        print("You have", chances, "chance(s) left. Better use 'em right this time!\n")
        letter = input('Take another guess. What is a letter that you think might be in the mystery word?\n')


else:
    while chances > 1:
        if letter.lower() in word:
            print("Yes! That letter is in the word\n")
        else:
            print("No! That letter is NOT in the word\n")
        chances -= 1
        print("You have", chances, "chance(s) left\n")
        letter = input('Take another guess. What is a letter that you think might be in the mystery word?\n')

if letter.lower() in word:
            print("Yes! That letter is in the word\n")
else:
            print("No! That letter is NOT in the word\n")

guess = input(
    """
        Your chances are done! 
           The time is now! 
          WHAT IS THE WORD?\n
    """)  

if guess == correct:
    print("\nThat is the correct word. Congratulations! You have won the game.")
else:
    print("\nINCORRECT. You lost the game! BOOOOOOOO! GET OFF THE STAGE!\n")