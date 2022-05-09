from constants import *
from extra_functions import create_life_path_ssmls, find_all, reduction, total, url_scrape, name_calc
from os import system, name
from googletrans import Translator

translator = Translator()

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

#Life path
personal_year = ""
clear()
print("       ***      ZULTAN L'ÉTRANGE, VOUS SALUE!     *** ")
print("  !!! DITES-MOI VOTRE DATE DE ANNIVERSAIRE, ET JE VOUS DIRAIS CE QUI SE PASSE !!!\n\n")
birth_date = input("ENTREZ VOTRE DATE DE NAISSANCE (YYYYMMDD): ")
personal_year = birth_date[-1] + birth_date[-2] + birth_date[-3] + birth_date[-4] + birth_date[0:4]
birth_day = birth_date[-2] + birth_date[-1]

while len(birth_date) != 8:
    try:
        birth_date = input("ENTREZ VOTRE DATE DE NAISSANCE (YYYYMMDD): ")
    except:
        print("Veuillez écrire sous forme YYYYMMDD (8 chiffres)")

life_path = reduction(birth_date, PYTHAGOREAN_ALPHABET)
personal_year = reduction(personal_year, PYTHAGOREAN_ALPHABET)

print("\nYour life path number is:", life_path)
my_texts = url_scrape("https://creativenumerology.com/life-path-number/" + str(reduction(str(life_path),PYTHAGOREAN_ALPHABET)) + "-destiny-path/")
my_text = my_texts[0]
my_list = my_texts[1]

# Choose if you want it read aloud
choice = ""

while choice not in POS_CHOICES or choice not in NEG_CHOICES:      
        choice = input("\nAimeriez-vous que votre numéro de chemin de vie soit lu pour vous?\n(oui/non): ").lower()

        if choice in POS_CHOICES:
            # Create ssml to read aloud
            #print(my_text)
            create_life_path_ssmls(my_text,life_path)

            # Gather all the ssml's for the number in the list
            #ssml_list = find_all(str(life_path),'../')
            #print(ssml_list)

            # Read it - if it's too large for the synthesize buffer, read one after another.
            ssml_string = open("life_path_" + str(life_path) + "_1" + ".xml", "r").read()
            #print(ssml_string)
            speech_synthesizer.speak_ssml_async(ssml_string).get()

            # Read it - if it's too large for the synthesize buffer, read one after another.
            ssml_string = open("life_path_" + str(life_path) + "_2" + ".xml", "r").read()
            #print(ssml_string)
            speech_synthesizer.speak_ssml_async(ssml_string).get()

        elif choice in NEG_CHOICES:
            for paragraph in my_list:
                print(paragraph,end="\n\n")
        else:
            print("Réessayez, cette fois !")
            continue


print("Votre année personnelle est:", personal_year)
print("Votre numéro de jour de naissance est:",birth_day,"et représente", BIRTH_DAY[int(birth_day.replace("0",""))],"\n")

#Destiny number
destiny_number = ""
soul_urge_number = ""
personality_number = ""

full_name = input("Ecrivez votre nom complet, y compris le deuxième prénom qui vous a été donné à la naissance\nNOM COMPLET À LA NAISSANCE:").lower().replace(" ", "")
print("\nNOM COMPLET ENTRE:",full_name,total(full_name,PYTHAGOREAN_ALPHABET),reduction(full_name, PYTHAGOREAN_ALPHABET))

name_list = full_name.split()
nr_names = len(name_list)

name_vals = name_calc(name_list, PYTHAGOREAN_ALPHABET)


print("Valeurs de nom",name_vals)
#print("Destiny number",destiny_number,reduction(destiny_number),"Soul Urge:",soul_urge_number,total(soul_urge_number),reduction(soul_urge_number),"Personality:",personality_number,total(personality_number),reduction(personality_number))

destiny_number = reduction(name_vals[0], PYTHAGOREAN_ALPHABET)
soul_urge_number = reduction(name_vals[1], PYTHAGOREAN_ALPHABET)
personality_number = reduction(name_vals[2], PYTHAGOREAN_ALPHABET)

print("\nVotre numéro Destiny/Expression est:", destiny_number)
print("Votre nombre Soul Urge / Soul Desire / Heart Desire est:", soul_urge_number)
print("Votre numéro de personnalité est :", personality_number)
