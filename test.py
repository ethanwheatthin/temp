import json

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os.path
import pymysql

mydb = ''


def connect_to_DB():
    global mydb
    mydb = pymysql.connect("ethan.cikeys.com", "ethancik_home", "Rebels19!", "ethancik_LineDance")
    return mydb.cursor()


def insert_into_DB(cursor, dance_name, dance_difficulty, dance_count, dance_walls, dance_music, dance_sheet,
                   dance_choreographer):
    global mydb
    query = "INSERT INTO StepSheets(dance_name,level,walls,step_count,step_sheet,choreographer,music) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    values = (dance_name, dance_difficulty, dance_walls, dance_count, dance_sheet, dance_choreographer, dance_music)
    cursor.execute(query, values)
    mydb.commit()


if __name__ == "__main__":
    cursor = connect_to_DB()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = Chrome("C:\\Users\\Ethan\\Desktop\\LineDance\\chromedriver.exe")
    link = "https://www.copperknob.co.uk/stepsheets/american-kids-ID98907.aspx"
    # driver.get("https://www.copperknob.co.uk/search.aspx?Order=Alphabetical&Lang=en&SearchType=Title&Level=Beginner&Beat=-1&Wall=-1&Search=&recnum=20")

    # driver.get("https://www.copperknob.co.uk/search.aspx?Order=Alphabetical&Lang=en&SearchType=Title&Level=Beginner&Beat=-1&Wall=-1&Search=&recnum=0")
    # title = driver.find_elements_by_xpath("//a[@href]")
    save_path = "C:\\Users\\Ethan\\Desktop\\MasterLineDances\\BeginnerLineDances"
    dance_links = open("C:\\Users\\Ethan\\Desktop\\LineDance\\BeginnerDanceLinks.txt")
    # os.chdir(save_path)
    key = 6772
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
            dance_choreographer = \
            str(driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[3]/div[3]/div[4]").text).split(':')[1].replace(
                "\n", "")
            dance_music = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[3]/div[3]/div[5]/span").text
            dance_sheet = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[3]/div[4]/div[1]").text

            insert_into_DB(cursor, dance_name, dance_difficulty, dance_count, dance_walls, dance_music, dance_sheet,
                           dance_choreographer)

            key += 1
            print(str(key) + ": Finished Link => " + line + "\n")
        except:
            print("Error on this link: " + line)
            break
