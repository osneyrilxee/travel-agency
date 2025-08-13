import time
import random

#Madlibs game

destination = ("Where do you want to go? ")


def madlibsgame(destination=None):
    # time.sleep(2)
    objet = str(input("Choose an object: "))
    emotions = ["stupid", "happy", "exhausted", "lovely"]
    emotion = input("Which emotion you choose? ("+", ".join(emotions)+") ")
    animals = str(input("Choose an animal: "))
    verb = str(input("Choose a verb: "))

    if destination:
        print(f"On your trip to {destination}, you will see a giant {animals}"
              f" and a/an {objet}, and you felt so {emotion} you started {verb}ing")
    else:
        print(f"On your future trip, you will see a giant {animals}"
              f" and a/an {objet}, and you felt so {emotion} you started {verb}ing")
        
        # must find solution to make appear the destination value if the user entered a destination before

#Mysterious Number Game

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
            

#Name step

name = input("Enter your name: ")

# name condition for the next step
if name.isdigit():
    print("Please enter your name with character!")
elif name == "":
    print("Please, don't let the input empty!")
    exit()
    #must be repeat the code as long as the input isn't fill with string value IMPORTANT!!!!!!!!

#Variable

age = "Enter you age: "
countries = {
    "korea" : 850,
    "south korea": 850,
    "south of korea": 850,
    "south korea": 850,
    "italy": 550,
    "thailand": 790
}

# main condition

while age.isdigit:
    age = input("Enter you age: ")
    try:
        #convert age to int variable
        if int(age) < 18:
            print("You can't travel! You must be 18. I am sorry dear user!")
            question()
        elif int(age) >= 18:
            #condition if the user has 18 or more

            while True:
                destination = input("Where do you want to go? (South of korea, Italy or Thailand): ")


                destination = destination.lower()

                if destination in countries:
                    #Which countries
                    print(f"Welcome to our company")
                    break
                else:
                    print("please answer to the question")
                    continue

            while True:
                
                distance = {
                    "france": 0,
                    "korea": 12800,
                    "south of korea": 12800,
                    "south korea": 12800,
                    "italy": 1424,
                    "thailand": 9510
                }

                travellers = input("How many travellers are you? ")
                if travellers.isdigit():
                    price = countries[destination]
                    travellers = int(travellers)
                    total_price = countries[destination] * travellers
                    distance_process = abs(distance["france"]) + (distance[destination])
                    print(f"The {destination}'s travelling cost "
                    f"${price} but you are {travellers} so it costs ${total_price}. "
                    f"I wish you a good travel approximately {distance_process}km")
                    break
                else:
                    continue

            
        #question for games
        question()
        
    except ValueError:
            print("Please enter an integer number")
            continue
else:
    print("you're different")
        