import os
from constants import *
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def create_life_path_ssml(text, life_path):
    # Create new ssml for life path number
    ssml_txt = '<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US"><voice name="en-US-BrandonNeural"><prosody rate="-20%" pitch="-10%">\n'
    ssml_txt += text + "\n"
    ssml_txt += '</prosody></voice></speak>'

    if os.path.isfile("life_path_" + str(life_path) + ".xml"):
        print("The ssml for this life_path number already exists!")
        print("Using Cached version.")
        pass
    else:
        with open("life_path_" + str(life_path) + ".xml",'w') as file:
            file.write(ssml_txt)

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
        title = res.findAll("span")

        for tag in tags:
            p.append(tag.getText().lower())

    p = p[1:-11]
    p.insert(0,title[4].getText().lower())
    
    for paragraph in p:
        text += paragraph
    
    return (text,p)

def name_calc(name_list, alphabet):
    destiny_number = ""
    soul_urge_number = ""
    personality_number = ""

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
    buf = 0

    for digit in birth_date:
        try:
            if digit.isdigit():
                buf += int(digit)
            elif digit.isalpha:
                buf += int(alphabet[digit])
            else:
                continue
        except:
            print("Something is wrong with reduction data!")

        if buf not in MASTER_NUMBERS:
            while len(str(buf)) > 1:
                buf = int(str(buf)[0]) + int(str(buf)[1])

    return buf