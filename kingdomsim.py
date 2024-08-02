#Basically a ruler roleplay game
import colorama
import time
import random
from colorama import Fore, Style
money = 0
Raid = False
Store = False
Inventory = False
Food_Supply = 100
Happinness = 100
Days_lived = 0
population = 100
Wood = 100
Stone = 100


    
 #This is just a 50 50 system for better randomness
def start_game():
    villager_request = 0.9
    print(Fore.CYAN + """
         Hey there, we just lost 
          our king, and would like you
          to become our new king,
          You got this!
          
""" + Style.RESET_ALL)
    time.sleep(0.3)
    name = input("What should we call you? ")
    print(f"Thank you for taking this role, King {name}!")
    print(Fore.YELLOW + """
--CONTROLS--
          INV - Opens inventory and shows stats
          Shop - Opens shop
          """ + Style.RESET_ALL)
    



    print("")
    time.sleep(0.4)
    villager_chance()
    if villager_chance():
        event_occurance()
    else:
        print("No villagers appeared today!")

    
def natural_disaster_chance():
    natural_disaster_spawn = 0.40
    rand = random.random()
    if natural_disaster_spawn > rand:
        return True
    else:
        return False
def natural_disaster_system():
    if natural_disaster_chance():
        print(Fore.RED + "A natural disaster is happening, hope you're well prepared!" +Style.RESET_ALL)
        Food_Supply -= 15
    


def villager_chance(): #function for chance for villagers to spawn in
    villager_request = 0.20
    rand = random.random()
    if villager_request > rand:
        
        return True
    else:
        return False
    
def specific_villager_event():
    Villager = ["wood","stone","friends"]
    
     #types of occurances
    random_villager_event = random.choice(Villager) #randomizes it
    if random_villager_event == "wood" and villager_chance: 
        wood()
    elif random_villager_event == "stone" and villager_chance:
        stone()
    elif random_villager_event == "friends":
        friends()

        
def event_occurance():
    if villager_chance: #If a villager spawns, then
        print(Fore.YELLOW + "A villager comes before you!" + Style.RESET_ALL)
        specific_villager_event()
    
def wood():
    chance = random.randint(0, 1)

    wood_response = input("Do you say Y/N? ") #randomness for the user reply for wood
    if chance == 1 and wood_response == "Y" and specific_villager_event == "wood":
        print("You gave them wood, and they rewarded you handsomely!")
        money +=50
        Wood -= 10
    elif chance == 0 and wood_response == "Y" and specific_villager_event == "wood":
        print("You gave them wood, but got nothing in return.")
        Wood -=10
    elif chance == 1 and wood_response == "N" and specific_villager_event == "wood":
        print("You didn't give them wood and you lost a lot of people, they moved out")
        people -=15
    else:
        print("He gave you more people!")
        population +=10
def stone():
    chance = random.randint(0, 1)
    stone_response = input("Do you say Y/N? ") #randomness for the user reply for wood
    if chance == 0 and stone_response == "Y" and specific_villager_event == "stone":
        print("You gave them stone, and they rewarded you handsomely!")
        money+=76
        stone -= 15
    elif chance == 1 and stone_response == "Y" and specific_villager_event == "stone":
        print("You gave them stone, but got nothing in return.")
        stone -= 10
    elif chance == 1 and stone_response == "N" and specific_villager_event == "stone":
        print("You didn't give them stone and you lost a lot of people, they moved out")
        population-=15
    else:
        print("He gave you more people!")
        population +=14

def friends():
    chance = random.randint(0, 1)
    stone_response = input("Do you say Y/N? ") #randomness for the user reply for wood
    if chance == 1 and stone_response == "Y" and specific_villager_event == "friends":
        print("You let them stay, and they rewarded you handsomely!")
        money += 46
    elif chance == 1 and stone_response == "Y" and specific_villager_event == "friends":
        print("You let them stay, but got nothing in return.")
    elif chance == 0 and stone_response == "N" and specific_villager_event == "friends":
        print("You let them stay and you lost a lot of people, they moved out")
        population -= 20
    else:
        print("He gave you more people!")
        population += 50

start_game()

def achievement_tracker():
    if population == 150:
        achievements.append("Getting Bigger")

def shop_system():
    print(Fore.YELLOW + """
    WELCOME TO THE KINGDOM SHOP:                                         |
          [HURRICANE SIREN] - Prepares your kingdom for bad weather [20] |
          [WOOD REQUEST] - Sends out villagers to fetch you wood [10]    |
          [STONE REQUEST] - Sends out villagers to fetch you stone [15]  |
          [INFASTRUCTURE UPDATE] - Strengthens your city buildings [30]  |
__________________________________________________________________________





""")





def main_game_loop():
    global Days_lived
    start_game()
    while True:
        user_input = input("Enter your desired action here: ").upper()
        
        if user_input == "SHOP":
            shop_system()
        else:
            event_occurrence()
            natural_disaster_system()
            achievement_tracker()
            Days_lived += 1

    