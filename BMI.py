import colorama
import random
from colorama import Fore, Style
#BMI CALCULATER PROJECT

height_input = float(input("Enter your height (in inches)"))



weight_input = float(input(Fore.CYAN +"How much do you weigh? (In Pounds)" + Style.RESET_ALL))
#BMI Calculator, might be slightly off due to off factors such as age and gender
bmi = (weight_input * 703) / (height_input * height_input)


#Tells you your current bmi
print(Fore.GREEN + f"Your current BMI is {bmi}" + Style.RESET_ALL)

#Based off of the World health organisation, this is what your results mean, and this function displays that.
def bmi_result():
    if bmi < 18.5:
        print(Fore.RED + "YOU ARE UNDERWEIGHT!!! BULK" + Style.RESET_ALL)
    elif 25 < bmi < 30:
        print(Fore.YELLOW + "You are overweight, please cut a bit" + Style.RESET_ALL)
    elif 18.5 < bmi < 25:
            print(Fore.GREEN + "Just right, you are a legend." + Style.RESET_ALL)
    elif 30 < bmi < 35:
            print(Fore.LIGHTRED_EX + "You are severely overweight" + Style.RESET_ALL)
    elif 35 < bmi < 40:
            print(Fore.RED + "You are Obese" + Style.RESET_ALL)
    elif 40 < bmi < 50:
            print(Fore.MAGENTA + "You are morbidly obese." + Style.RESET_ALL)



bmi_result()