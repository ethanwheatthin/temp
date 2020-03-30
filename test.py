import json

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os.path
from random import randint

import firebase_admin
from firebase_admin import db

from firebase_admin import credentials


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


#def get_new_key()

if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = Chrome("/Users/EthanCC/Desktop/temp/chromedriver")
    link = "https://www.copperknob.co.uk/stepsheets/american-kids-ID98907.aspx"
    # driver.get("https://www.copperknob.co.uk/search.aspx?Order=Alphabetical&Lang=en&SearchType=Title&Level=Beginner&Beat=-1&Wall=-1&Search=&recnum=20")

    # driver.get("https://www.copperknob.co.uk/search.aspx?Order=Alphabetical&Lang=en&SearchType=Title&Level=Beginner&Beat=-1&Wall=-1&Search=&recnum=0")
    # title = driver.find_elements_by_xpath("//a[@href]")
    #save_path = "C:\\Users\\Ethan\\Desktop\\MasterLineDances\\BeginnerLineDances"
    dance_links = open("/Users/EthanCC/Desktop/temp/BeginnerDanceLinks.txt")

    usedKeys = open('UsedKeys.txt', 'a')
    usedKeysList = []
    cred = credentials.Certificate("/Users/EthanCC/Downloads/linedance-f12c4-firebase-adminsdk-aizzs-a0fcca8688.json")
    # firebase_admin.initialize_app(cred)
    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://linedance-f12c4.firebaseio.com/'
    })

    #os.chdir(save_path)
    counter = 0

    for line in dance_links:

        try:
            data = {}
            # driver = Chrome("/Users/EthanCC/Desktop/LineDance/chromedriver",chrome_options=chrome_options)
            driver.get(line)
            # driver.implicitly_wait(5)
            time.sleep(1)
            dance_name = driver.find_element_by_xpath("/html/body/div[5]/div/div[3]/div[1]/h2").text
            dance_count = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[3]/div[3]/div[1]/span").text
            dance_walls = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[3]/div[3]/div[2]/span").text
            dance_difficulty = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[3]/div[3]/div[3]/span").text
            dance_choreographer = str(driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[3]/div[3]/div[4]").text).split(':')[1].replace("\n","")
            dance_music = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[3]/div[3]/div[5]/span").text
            dance_sheet = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[3]/div[4]/div[1]").text

            ref = db.reference('Dance_Details').child("DanceID_" + str(counter))
            ref.set({
                "Dance_Name": dance_name,
                "Dance_Count": dance_count,
                "Dance_Walls": dance_walls,
                "Dance_Difficulty": dance_difficulty,
                "Dance_Choreographer": dance_choreographer,
                "Dance_Music": dance_music,
                "Dance_Steps": dance_sheet

            })

            counter += 1
            print(str(counter) + ": ")
            print(ref.get())
        except:
            print("Error on this link: " + line)
            break


