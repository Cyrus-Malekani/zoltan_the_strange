from constants import *
from extra_functions import create_life_path_ssmls, find_all, reduction, total, url_scrape, name_calc
from os import system, name

# Clear screen function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#Text to speech engine init
import azure.cognitiveservices.speech as speechsdk
my_key = "efbda9688be545df8d74bfdee2230c95"
my_region = "northeurope"
speech_config = speechsdk.SpeechConfig(subscription=my_key, region=my_region)
speech_config.set_property_by_name("voice","fr-FR-DeniseNeural")

# Creates a speech synthesizer using the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# Intro text
clear()
print("       ***      ZOLTAN THE STRANGE, GREETS YOU!      *** ")
print("  !!! TELL ME YOUR BIRTHDATE, AND I WILL TELL YOU WHAT'S UP !!!\n\n")
birth_date = input("ENTER YOUR BIRTHDATE (YYYYMMDD): ")

# Current year is 2022 = 2+2+2 = 6
personal_year = 6

birth_day = birth_date[-2] + birth_date[-1]

while len(birth_date) != 8:
    try:
        birth_date = input("ENTER YOUR BIRTHDATE (YYYYMMDD): ")
    except:
        print("Please use the form: YYYYMMDD (8 digits)")

life_path = reduction(birth_date, PYTHAGOREAN_ALPHABET)
personal_year += reduction(birth_date[4:], PYTHAGOREAN_ALPHABET)

print("\nYour life path number is:", life_path)
my_texts = url_scrape("https://creativenumerology.com/life-path-number/" + str(reduction(str(life_path),PYTHAGOREAN_ALPHABET)) + "-destiny-path/")
my_text = my_texts[0]
my_list = my_texts[1]

# Choose if you want it read aloud
choice = ""

while choice not in CHOICES:      
        choice = input("\nWould you like to have your life path number read for you?\n(yes/no): ").lower()

        if choice == CHOICES[0] or choice == CHOICES[1]:
            # Create ssml to read aloud
            create_life_path_ssmls(my_text,life_path)

            # Gather all the ssml's for the number in the list
            ssml_list = find_all(str(life_path),'../')
            print(ssml_list)
            
            for i in range(1,len(ssml_list)+1):
                ssml_string = open("life_path_" + str(life_path) + "_" + i + ".xml", "r").read()


            # Read it - if it's too large for the synthesize buffer, read one after another.
            #ssml_string = open("life_path_" + str(life_path) + "_1" + ".xml", "r").read()
            #speech_synthesizer.speak_ssml_async(ssml_string).get()

            # Read it - if it's too large for the synthesize buffer, read one after another.
            #ssml_string = open("life_path_" + str(life_path) + "_2" + ".xml", "r").read()
            #speech_synthesizer.speak_ssml_async(ssml_string).get()

        elif choice == CHOICES[2] or choice == CHOICES[3]:
            for paragraph in my_list:
                #print(paragraph,end="\n\n")
                pass
        else:
            print("Try again!")
            continue


print("Personal year number:", personal_year)
print("Birth day number:", birth_day,"and it represents;", BIRTH_DAY[int(birth_day.replace("0",""))],"\n")

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

print("\nYour Destiny/Expression number is:", destiny_number)
print("Your Soul Urge/Soul Desire/Heart Desire number is:", soul_urge_number)
print("Your Personality number is:", personality_number)
