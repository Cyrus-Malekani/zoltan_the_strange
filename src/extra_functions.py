import os
from re import S
from constants import *
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from gtts import gTTS
import os
import playsound

def speak(text):
    tts = gTTS(text=text, lang='en')

    filename = "zoltan_reading.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def create_life_path_ssmls(text, life_path):
    # Create new ssml for life path number
    SSML_HEADER = '<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US"><voice name="en-US-BrandonNeural"><prosody rate="-20%" pitch="-10%">\n' 
    SSML_FOOTER = '</prosody></voice></speak>'

    buf = ""
    
    for letter in text:
        if letter == '.':
            buf += '. '
        elif letter == '!':
            buf += '! '
        elif letter == '?':
            buf += '? '
        else:
            buf += letter

    text = buf

    txt1 = text[:len(text)//2]
    txt2 = text[len(text)//2:]

    ssml_txt1 = SSML_HEADER + txt1 + "\n" + SSML_FOOTER
    ssml_txt2 = SSML_HEADER + txt2 + "\n" + SSML_FOOTER

    if os.path.isfile("life_path_" + str(life_path) + ".xml"):
       # print("The ssml for this life_path number already exists!")
       # print("Using Cached version.")
        pass
    else:
        with open("life_path_" + str(life_path) + "_1" + ".xml",'w') as file:
            file.write(ssml_txt1)
        with open("life_path_" + str(life_path) + "_2" + ".xml",'w') as file:
            file.write(ssml_txt2)

def url_scrape(url):
    p = []
    text = ""

    try:
        html = urlopen(url)

    except HTTPError as e:
        print(e)

    except URLError:
        print("Server down or incorrect domain")

    else:

        res = BeautifulSoup(html.read(),"html5lib")
        tags = res.findAll("p")
        title = res.findAll ("span")

        for tag in tags:
            text = tag.getText().lower()
            p.append(tag.getText().lower())

    #print("p before:", p)
    p = p[1:-11]
   
    p.insert(0,title[4].getText().lower())
    #print("\n\n###\n\n")
    #print("p after:", p)
    
    for paragraph in p:
        text += paragraph
    
    return (p)

def name_calc(name_list, alphabet):
    destiny_number = ""
    soul_urge_number = ""
    personality_number = ""
    family_number = ""

    for name in name_list:
        for letter in name:
            if letter.isalpha():
                destiny_number += str(alphabet[letter])
            else:
                continue
            
            if letter in VOWELS:
                soul_urge_number += letter
            else:
                personality_number += letter

    return (destiny_number, soul_urge_number, personality_number)

def total(s,alphabet):
    res = 0
    for letter in s:
        if letter.isalpha():
            res += alphabet[letter]
    
    return res

def reduction(birth_date,alphabet):
    d = 0

    for digit in birth_date:
        try:
            if digit.isdigit():
                d += int(digit)
            elif digit.isalpha:
                d += int(alphabet[digit])
            else:
                continue
        except:
            print("Something is wrong with reduction data!")

        if d not in MASTER_NUMBERS:
            while len(str(d)) > 1:
                d = int(str(d)[0]) + int(str(d)[1])

    return d
