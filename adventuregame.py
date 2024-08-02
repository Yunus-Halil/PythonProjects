import time
import random
import colorama
from colorama import Fore, Back, Style

fish_count = 0
inventory_open = False
shop = False
health = 100
coins = 0
damage = 1
fishing = False
level = 1
experience = 0
agility = 0
strength = 0
points = 0
print(Fore.MAGENTA + "----WELCOME TO THIS TEXT-BASED ADVENTURE GAME----" + Style.RESET_ALL)

# Function to display player stats
def display_stats():
    global fish_count, coins, damage, health, strength, agility, experience, level, points
    print(Fore.CYAN + """
╔═════════════════════════════╗
║         PLAYER STATS        ║
╠═════════════════════════════╣
║ Level: {level}║
║ Experience: {level}║
║ Agility: {agility}║
║ Strength: {strength}║
║ Points: {points}║
╚═════════════════════════════╝
    """.format(level=level, experience=experience, agility=agility, strength=strength, points=points) + Style.RESET_ALL)

def death_system():
    global health
    if health <= 20:
        print(Fore.RED + "Critically low, please heal!" + Style.RESET_ALL)
    if health <= 80:
        print(Fore.YELLOW + "Ouch!" + Style.RESET_ALL)
    if health <= 60:
        print(Fore.YELLOW + "A fracture!!" + Style.RESET_ALL)
    if health == 0:
        print(Fore.RED + "YOU DIED!" + Style.RESET_ALL)

def shop_system():
    global user_input, coins, damage, fishing, health, shop, fish_count

    print(Fore.YELLOW + "Welcome to the shop! You have " + str(coins) + " coins.")
    print(Fore.GREEN + """
          Sword = 5 coins, increases your damage!
          Fishing rod = 10 coins, allows you to fish for food
          Medkit = 5 coins, heals you by 15 health 
          You can sell fish for 2 coins! (sell_fish)
          Q - Exit shop
          """ + Style.RESET_ALL)

    while True:
        user_input = input("Enter your choice: ").strip()
        if user_input == "Sword":
            if coins >= 5:
                damage += 4
                coins -= 5
                print(Fore.CYAN + "You have bought a sword, damage increased!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Not enough coins!!" + Style.RESET_ALL)
        elif user_input == "Fishing_rod":
            if coins >= 10:
                fishing = True
                coins -= 10
                print(Fore.CYAN + "You have unlocked fishing!!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Not enough coins!!" + Style.RESET_ALL)
        elif user_input == "Medkit":
            if coins >= 5:
                health += 15
                coins -= 5
                print(Fore.CYAN + "You have bought a medkit, health increased!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Not enough coins!!" + Style.RESET_ALL)
        elif user_input == "sell_fish":
            if fish_count > 0:
                fish_count -= 1
                coins += 2
                print(Fore.GREEN + "You sold a fish, you know have " + str(coins) + " coins and " + str(fish_count) + " fish!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "You got no fish buddy..." + Style.RESET_ALL)

        elif user_input == "Q":
            print(Fore.YELLOW + "Exiting shop..." + Style.RESET_ALL)
            shop = False
            break
        else:
            print(Fore.RED + "Invalid input!!" + Style.RESET_ALL)

def explore():
    global health, coins, damage, shop, fishing, fish_count
    print(Fore.GREEN + "You have chosen to explore!" + Style.RESET_ALL)
    if spawn_monster():
        print(Fore.RED + "A Wild Monster Has Appeared!" + Style.RESET_ALL)
        health -= 15
        print(Fore.YELLOW + "You have lost some health, your new health is " + str(health) + Style.RESET_ALL)
        coins += 1
    elif spawn_monster() and damage > 3:
        print(Fore.GREEN + "You luckily have a sword, and you swiftly fight the monster!")
        print(Fore.YELLOW + "You have lost some health, your new health is " + str(health) + Style.RESET_ALL)
        print(Fore.YELLOW + "You still get some bruises, but hey, nothing too much! Good job champ!" + Style.RESET_ALL)
        health -= 5
        coins += 1

        print(Fore.GREEN + "Luckily you gained 1 coin!" + Style.RESET_ALL)
    elif chest_chance():
        print(Fore.YELLOW + "You have found a chest! + 5 coins!" + Style.RESET_ALL)
        coins += 5
    elif lake_chance():
        print(Fore.CYAN + "You have found a lake to fish in")
        if fishing:
            print(Fore.MAGENTA + "You fish, and catch a fish!" + Style.RESET_ALL)
            fish_count += 1
        else:
            print(Fore.RED + "You dont have a fishing rod and cant catch anything! Visit the shop, please." + Style.RESET_ALL)
    else:
        print(Fore.LIGHTBLUE_EX + "You didn't find anything, but you didn't lose anything either!" + Style.RESET_ALL)

def spawn_monster():
    spawn_chance = 0.25
    return random.random() < spawn_chance

def inventory():
    global health, damage, coins, fishing, inventory_open, fish_count
    print(Fore.CYAN + "Your health is " + str(health) + Style.RESET_ALL)
    print(Fore.GREEN + "Your fishing status is " + str(fishing) + Style.RESET_ALL)
    print(Fore.YELLOW + "You have " + str(coins) + " coins" + Style.RESET_ALL)
    print(Fore.MAGENTA + "You deal " + str(damage) + " damage!" + Style.RESET_ALL)
    print(Fore.RED + "TYPE EXIT to get out of inventory" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "You have " + str(fish_count) + " fish")
    user_input = input().strip().lower()
    if user_input == "exit":
        inventory_open = False

def user_movements():
    global user_input, shop, inventory_open
    if user_input.lower() == "inventory":
        display_stats()
        inventory()
    elif user_input.lower() == "shop":
        shop = True
        shop_system()
    elif user_input.lower() == "explore":
        explore()
    
    else:
        print(Fore.RED + "Invalid action!" + Style.RESET_ALL)

def chest_chance():
    spawn_chance2 = 0.30
    return random.random() < spawn_chance2

def lake_chance():
    spawn_chance3 = 0.50
    return random.random() < spawn_chance3

# Example call to user_movements


while health > 0:
    user_input = input("What would you like to do? (explore/shop/inventory): ").strip().lower()
    user_movements()
    death_system()
    
