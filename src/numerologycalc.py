import unicodedata
import pyttsx3

from constants import *
from extra_functions import reduction, total, url_scrape, name_calc, speak
from os import system, name

# Speech engine
engine = pyttsx3.init()

# Clear screen function
def clear():
    system('cls')
    system('clear')
    

#Life path
personal_year = ""
clear()
print("       ***      ZOLTAN THE STRANGE, GREETS YOU!      *** ")
print("  !!! TELL ME YOUR BIRTHDATE, AND I WILL TELL YOU WHAT'S UP !!!\n\n")
birth_date = input("ENTER YOUR BIRTHDATE (YYYYMMDD): ")

personal_year = 6

birth_day = birth_date[-2] + birth_date[-1]

while len(birth_date) != 8:
    try:
        birth_date = input("ENTER YOUR BIRTHDATE (YYYYMMDD): ")
    except:
        print("Please write in this form YYYYMMDD (8 numbers)")

life_path = reduction(birth_date, PYTHAGOREAN_ALPHABET)
life_path_paragraphs = []

personal_year += reduction(birth_date[4:], PYTHAGOREAN_ALPHABET)



print("\nYour life path number is:", life_path)
my_texts = url_scrape("https://creativenumerology.com/life-path-number/" + str(reduction(str(life_path),PYTHAGOREAN_ALPHABET)) + "-destiny-path/")
#print("\n\nScraped the following:", my_texts)

for paragraph in my_texts:
    #print("\n\n" + paragraph)
    life_path_paragraphs.append(unicodedata.normalize('NFKD', paragraph))

#print("\n\nParagraph list includes:", life_path_paragraph_list)

#print("\n\nLength of my_texts:", len(my_texts))

# Choose if you want it read aloud
choice = ""

while choice not in CHOICES:      
        choice = input("\nWould you like to have your life path number read for you?\n(yes/no): ").lower()

        if choice == CHOICES[0] or choice == CHOICES[1]:
            for paragraph in life_path_paragraphs:
                speak(paragraph)
                input("Continue? (y/n): ")

        elif choice == CHOICES[2] or choice == CHOICES[3]:
            for paragraph in life_path_paragraphs:
                print(paragraph,end="\n\n")
                pass
        else:
            print("Try again")
            continue


print("Your personal year is:", personal_year)
print("Your birth day is:",birth_day,"and it represents", BIRTH_DAY[int(birth_day.replace("0",""))],"\n")

#Destiny number
destiny_number = ""
soul_urge_number = ""
personality_number = ""

full_name = input("Write your full name including middle name given to you at birth\nFULL NAME AT BIRTH:").lower().replace(" ", "")
print("\nENTERED FULLNAME:",full_name,total(full_name,PYTHAGOREAN_ALPHABET),reduction(full_name, PYTHAGOREAN_ALPHABET))

name_list = full_name.split()
nr_names = len(name_list)

name_vals = name_calc(name_list, PYTHAGOREAN_ALPHABET)


print("Name values",name_vals)
#print("Destiny number",destiny_number,reduction(destiny_number),"Soul Urge:",soul_urge_number,total(soul_urge_number),reduction(soul_urge_number),"Personality:",personality_number,total(personality_number),reduction(personality_number))

destiny_number = reduction(name_vals[0], PYTHAGOREAN_ALPHABET)
soul_urge_number = reduction(name_vals[1], PYTHAGOREAN_ALPHABET)
personality_number = reduction(name_vals[2], PYTHAGOREAN_ALPHABET)
family_number = reduction(name_vals[0][-1], PYTHAGOREAN_ALPHABET)

print("\nYour Destiny/Expression number is:", destiny_number)
print("Your Soul Urge/Soul Desire/Heart Desire number is:", soul_urge_number)
print("Your Personality number is:", personality_number)
print("Family number: ", family_number )
