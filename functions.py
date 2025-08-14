import time
import random

def madlibsgame(destination=None):
    emotions = ["stupid", "happy", "exhausted", "lovely"]
    
    while True:
        objet = input("Choose an object: ")
        if objet.isalpha():
            break
        else:
            continue
        
    while True:
        emotion = input("Which emotion you choose? here's some example: ("+", ".join(emotions)+"): ")
        if emotion.isalpha():
            break
        else:
            continue
        
    while True:
        animals = input("Choose an animal: ")
        if animals.isalpha():
            break
        else:
            continue
        
    while True:
        verb = input("Choose a verb: ")
        if verb.isalpha():
            break
        else:
            continue
    
    

    if destination:
        print(f"On your trip to {destination}, you will see a giant {animals}"
              f" and a/an {objet}, and you felt so {emotion} you started {verb}ing")
    else:
        print(f"On your future trip, you will see a giant {animals}"
              f" and a/an {objet}, and you felt so {emotion} you started {verb}ing")
        
        # must find solution to make appear the destination value if the user entered a destination before

def mysteriousnumbergame():
    pick = random.randint(0, 1000)

    while True:
        try:
            user_input = int(input("Find the number between 0 - 1000: "))
        except ValueError:
            print("Please enter an integer number")
            continue

        if pick < user_input:
            print("lower")

        elif pick > user_input:
            print("higher")
        
        else:
            print(f"You won! The number was {pick}")
            break
        
def question():
    while True:
        game = input("Which game would you like to play? Madlibs or Mysterious Number: ")

        if game == "Madlibs" or game == "madlibs":
            print("You will soon play to Madlibs")
            time.sleep(2)
            print("Loading")
            time.sleep(5)
            print("Starting")
            time.sleep(1)
            madlibsgame()
            exit()

        elif game == "MN" or game == "mn" or game == "mysterious number" or game == "Mysterious Number" or game == "mysterious Number" or game == "Mysterious number":
            print("You will soon play to Mysterious Number")
            time.sleep(2)
            print("Loading")
            time.sleep(5)
            print("Starting")
            time.sleep(1)
            mysteriousnumbergame()
            exit()

        else:
            print("Please enter string character")
            continue