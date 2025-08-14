from functions import question

destination = ("Where do you want to go? ")
            
            
name = str("Please enter a valid name: ")
#Name step
while True:
    name = input("Please enter your name: ")
    if name.isalpha():
        break
    else:
        continue

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
        