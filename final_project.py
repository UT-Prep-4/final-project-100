#Name(s): kresley jessieann brookLynn kayla miah
#Final Project - Build Something Worth Showing Off
'''
This is the big one. At the end of camp you will demo this project at the
SHOWCASE, and it should be good enough to put on a resume or mention in a
college application. That means it is not just "code that works." It is a
project you designed, built, polished, and can explain.

WHAT MAKES IT SHOWCASE-WORTHY (the autograder checks for these):
  1. ORGANIZED: your code is split into clear, purposeful segments (functions optional), not one
     giant blob. (Aim for at least 3-4 functions with real jobs.)
  2. SUBSTANTIAL: this is a multi-day build, bigger than the mini-project.
  3. REAL LOGIC: decisions (if/elif/else) and repetition (loops) working together.
  4. DOCUMENTED: fill out PROJECT.md so a stranger (or a college admissions
     reader!) can understand what you built and how to run it.

Whether it is impressive, creative, and demo-ready is judged by humans at
showcase, not by the autograder.

============================= PICK YOUR TRACK =================================

TRACK A: IMAGE PROCESSING PROGRAM
  Build a program that opens an image and transforms it with a special
  function you write yourself: brightness adjustment, a color filter overlay,
  grayscale, mirror, pixelate, or invent your own effect.
  The Pillow library is preinstalled. The core moves:

      from PIL import Image
      img = Image.open("photo.png")
      width, height = img.size
      pixel = img.getpixel((x, y))          # (red, green, blue), each 0-255
      img.putpixel((x, y), (r, g, b))       # set a pixel
      img.save("output.png")                # then click it in VS Code to view!

  Brightness is a for loop over every pixel that multiplies r, g, b by a
  factor the user chooses (careful: values must stay between 0 and 255).
  A filter overlay nudges every pixel toward a color (add red, drop blue...).
  Level up: ask the user which effect to apply with input(), show a menu,
  process any image file they name, draw the result with turtle or pygame.

TRACK B: ADVENTURE GAME
  Build a text adventure where the player explores, makes choices, and wins
  or loses based on decisions and luck. Use random for surprises: treasure,
  traps, enemy encounters, dice rolls, critical hits.
  The shape of it: one function per location or scene, input() for choices,
  an inventory list, health or gold as numbers, and random.randint() for
  the unexpected. Level up: turn-based combat, a map, multiple endings,
  ASCII art title screens, a save-your-score high score.

TRACK C: YOUR OWN IDEA
  A bigger game (pygame or turtle), a quiz app, a tool that solves a real
  problem you have, a simulation, generative turtle art... Pitch it to your
  instructor FIRST, then build it. The four requirements above still apply.

=============================== PLAN FIRST ====================================
Before you write code, fill this in (it will keep you honest all week):

  MY PROJECT: (We created hangman.)
  THE PIECES I NEED TO BUILD: (Turtle, input, while loop)
  WHAT I WILL DEMO AT SHOWCASE: (We have created hangman in python. 
  We created our own word list and used turtle to display the actual person. 
  You guess a letter and have 4 lives. If you guess a wrong letter, you lose a life. 
  if you lose all your lives the game ends. If you guess the word correctly, you win!)

==============================================================================
Build your project below (and split it into more .py files if it gets big;
the grader reads all of them). Delete this line and start!
'''


basehangman = """|--------0
|        |
|        |
|
|
|
|
|
|
|
|
|
|___________________"""

onewrong = """|--------0
|        |
|        |
|    ( ' - ' )
|
|
|
|
|
|
|
|
|___________________"""

twowrong = """|--------0
|        |
|        |
|    ( ' - ' )
|        |
|        |
|        |
|        |
|        |
|
|
|
|___________________"""

threewrong = """|--------0
|        |
|        |
|     ( ' - ' )
|        |
|    /---|---\\
|      / | \\
|      / | \\
| |
|
|
|
|
|___________________"""

# miah is da goat
fourwrong = """|--------0
|        |
|        |
|    ( ' - ' )
|        |
|    /---|---\\
|      / | \\
|      / | \\
|        |
|       / \\
|       / \\
|.      / \\
|
|___________________"""

deadhangman = """|--------0
|        |
|        |
|   <( X ~ X )>
|        |
|    /---|---\\
|      / | \\
|      / | \\
|.       |
|       / \\
|       / \\
|       / \\
|
|___________________"""

hangmans=[onewrong, twowrong, threewrong, fourwrong, deadhangman]

wordlist = ["mermaid", "spodick", "unicorn", "ocean", "hippopotomonstrosesquipeliphobia"]
blank = "_"
lives = 4

print(basehangman)


while lives > 0: # what condition keeps the game going?

  for word in wordlist:  # loop through each word in wordlist

    revealed = [blank] * len(word)
    print("\n","="*20, "New game","="*20, "\n")
    print( basehangman, "\n")
    print("Amount of letters in word: ", len(word), "(", " _ " * len(word), ")")
    option = 0
    empty = []

    for letter in range(len(word)):  #  loop through each letter position in the word
        print("\n","="*50, "\n")
        guess = input("Enter a letter: ")
        letterbank = empty.append(guess)

        if guess in word:  # check if the guessed letter is in the word
            #  if it's also in the correct spot, print a message

            for i in range(len(word)):  #  loop through the word to reveal matching letters
                if guess == word[i]:  # check if this position matches the guess
                    revealed[i] = guess

        else:
            print("Letter not in word.")
            lives = lives-1
            if option == 4:
                break
            print(hangmans[option])
            print(letterbank)
            option = option+1
            #  handle a wrong guess (print message, lose a life,
            # check if out of guesses, show next hangman stage)
            pass

        print("\n", "".join(revealed))

    print()
    final = "".join(revealed)
    print("\n", "Your final word is:", final, "\n")

    if word == revealed:  # check if the revealed word matches the actual word
        print("","=============== You guessed correctly! You beat Hangman! ===============")
    else:
        print(deadhangman)
        print("X"*15, "You did not beat hangman", "X"*15, "\n")
    print()










