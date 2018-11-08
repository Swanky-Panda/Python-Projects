import random
from colorama import Fore

words = ("cheese", "head", "winning", "elimination", "placing", "quizzes", "learning", "studying", "scores", "principal", "bullies", "stapler", "books", "dictionary", "calculator")

points = 0

print(Fore.LIGHTRED_EX + """

          VRINCH'S WORD SCRAMBLE GAME

    Unscramble the letters to make a word.
(Press the enter key twice at any time to quit.)
"""
      + Fore.RESET)
print("\n")

play = input("Do you want to play? (yes or no): ")
while play == "yes":
    # pick one word randomly from the sequence
    word = random.choice(words)

    # create variable checking if guess is correct
    correct = word

    # create a scrambled version of the word
    scramble = ""
    while word:
        position = random.randrange(len(word))
        scramble += word[position]
        word = word[:position] + word[(position + 1):]

    # create the game
    print("The scramble is: " + Fore.WHITE + scramble + Fore.RESET)
    guess = input("\nYour guess: ")
    while guess != correct and guess != "":
        print(Fore.RED + "Sorry, that's not it. (-10 Points)" + Fore.RESET)
        print("\n" * 0)
        guess = input("Your guess: ")
        points = points - 10
    if guess == correct:
        print(Fore.LIGHTGREEN_EX + "Correct!!! (+ 5 Points)\n" + Fore.RESET)
        points = points + 5
        print("Your score is: " + Fore.WHITE + str(points) + Fore.RESET)
        print("\n")
    else:
        play = "no"

print(Fore.LIGHTRED_EX + """

          Thanks for playing, bye! 
""")

input("""
        Press the enter key to exit.
""")
