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



words= ["mermaid" , "spoddick" , "unicorn" , "ocean" , "hippopotomonstrosesquipedaliophobia"]
blank = "_"
lives = 4

while lives>0:
  for word in words:
    print(word)
    empty = ""
    for letter in range(len(word)):
      guess = input("Guess a letter: ")

      if guess in word:
        print("Correct Letter!")
        empty += word[letter]
        print(empty)
        print("~"*15)

      else:
        print("WRONG.")
        empty += blank
        lives = lives-1
        print(empty)
        print("~"*15)
        continue

    print(empty)
    print("~+*15")
    print("Starting next word!")
    print()

print(word)

  

'''
#import random, time
# Word band
# Pick a random word
RANDOM_WORD = random.choice(words)

guessed = ""
lives = 4
GAME_ACTIVE = True
while lives > 0:
  print("Welcome to Hangman!")
  print("")
  print("")
  print("")
  time.sleep(1.5)
  WORD_FOR_GAME = RANDOM_WORD
  LENGTH_OF_RAN_WORD = len(WORD_FOR_GAME)
  print("The Word Is: ", end = " ")
  for i in range(LENGTH_OF_RAN_WORD):
      print("_", end = " ")
  #\033c
  print("")
  print("")
  print("")
  CHAR_LIST = list(WORD_FOR_GAME)
  print(CHAR_LIST)
  print("")
  USER_GUESS = input("Guess a letter: ")



while USER_GUESS
for i in range(WORD_FOR_GAME):




      

  letter = USER_GUESS


  for letter in RANDOM_WORD:
    if letter in RANDOM_WORD:
      display = display + "_"

  print("/nWord:" , display)

      

  guess = input("Guess a letter: ")
  


  
    if lives == 0:
        print("/nGame Over!")
        print("The word was:" , words)
    elif guess in guessed:
        print("You already guessed that letter.")
    elif guess in words:
        print("Correct!")
        guessed = guessed + guess
    else:
        print("Wrong! HAHA")
        lives = lives - 1
        guessed = guessed + guess
        print("Lives left:" , lives)
    if display  == words:
      print("You won!")
        
  '''
