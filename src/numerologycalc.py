from constants import *
from extra_functions import create_life_path_ssml, reduction, total, url_scrape, name_calc

#Text to speech engine init
import azure.cognitiveservices.speech as speechsdk

my_region = "northeurope"
speech_config = speechsdk.SpeechConfig(subscription=my_key, region=my_region)
speech_config.set_property_by_name("voice","en-US-BrandonNeural")

# Creates a speech synthesizer using the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

#Life path
personal_year = ""
birth_date = input("Enter your birthdate (YYYYMMDD): ")
personal_year = birth_date[-1] + birth_date[-2] + birth_date[-3] + birth_date[-4] + birth_date[0:4]
birth_day = birth_date[-2] + birth_date[-1]

while len(birth_date) != 8:
    try:
        birth_date = input("Enter your birthdate (YYYYMMDD): ")
    except:
        print("Please write in form YYYYMMDD (8 digits)")

life_path = reduction(birth_date, PYTHAGOREAN_ALPHABET)
personal_year = reduction(personal_year, PYTHAGOREAN_ALPHABET)

print("\nYour life path number is:", life_path)
my_texts = url_scrape("https://creativenumerology.com/life-path-number/" + str(reduction(str(life_path),PYTHAGOREAN_ALPHABET)) + "-destiny-path/")
my_text = my_texts[0]
my_list = my_texts[1]

# Choose if you want it read aloud
choice = ""

while choice not in CHOICES:      
        choice = input("\nWould you like to have your life path number read for you? (y/n): ").lower()

        if choice == CHOICES[0]:
            # Create ssml to read aloud
            create_life_path_ssml(my_text,life_path)

            # Read it
            ssml_string = open("life_path_" + str(life_path) + ".xml", "r").read()
            speech_synthesizer.speak_ssml_async(ssml_string).get()

        elif choice == CHOICES[1]:
            for paragraph in my_list:
                print(paragraph,end="\n\n")
        else:
            continue


print("You're personal year number is:", personal_year)
print("You're birth day number is:",birth_day,"and stands for", BIRTH_DAY[int(birth_day.replace("0",""))],"\n")

#Destiny number
destiny_number = ""
soul_urge_number = ""
personality_number = ""

full_name = input("Write your full name including middle name: ").lower().replace(" ", "")
print("\nInputted FULLNAME:",full_name,total(full_name,PYTHAGOREAN_ALPHABET),reduction(full_name, PYTHAGOREAN_ALPHABET))

name_list = full_name.split()
nr_names = len(name_list)

name_vals = name_calc(name_list, PYTHAGOREAN_ALPHABET)


print("Name vals",name_vals)
#print("Destiny number",destiny_number,reduction(destiny_number),"Soul Urge:",soul_urge_number,total(soul_urge_number),reduction(soul_urge_number),"Personality:",personality_number,total(personality_number),reduction(personality_number))

destiny_number = reduction(name_vals[0], PYTHAGOREAN_ALPHABET)
soul_urge_number = reduction(name_vals[1], PYTHAGOREAN_ALPHABET)
personality_number = reduction(name_vals[2], PYTHAGOREAN_ALPHABET)

print("\nYour Destiny/Expression number is:", destiny_number)
print("Your Soul Urge/Soul Desire/Heart Desire number is:", soul_urge_number)
print("Your Personality number is:", personality_number)