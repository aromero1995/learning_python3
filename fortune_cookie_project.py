# Fortune Cookie Program 🥠

#set random number importer
import random

#set fortune variable to random integers
fortune = random.randint(0, 4)

#set fortune readings if else statements
if fortune == 0:
  print("May you find meaning to yourself")
elif fortune == 1:
  print("May your crops wither")
elif fortune == 2:
  print("You know the answer you seek")
elif fortune == 3:
  print("You may find that you know nothing")
elif fortune == 4:
  print("You are only you")
