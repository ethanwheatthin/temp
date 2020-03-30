from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os.path
import pymysql



if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = Chrome("/Users/EthanCC/Desktop/LineDance/chromedriver")
    link = "https://www.copperknob.co.uk/stepsheets/american-kids-ID98907.aspx"
    #driver.get("https://www.copperknob.co.uk/search.aspx?Order=Alphabetical&Lang=en&SearchType=Title&Level=Beginner&Beat=-1&Wall=-1&Search=&recnum=20")

    #driver.get("https://www.copperknob.co.uk/search.aspx?Order=Alphabetical&Lang=en&SearchType=Title&Level=Beginner&Beat=-1&Wall=-1&Search=&recnum=0")
    #title = driver.find_elements_by_xpath("//a[@href]")
    save_path = "C:\\Users\\Ethan\\Desktop\\MasterLineDances\\BeginnerLineDances"
    dance_links = open("C:\\Users\\Ethan\\Desktop\\LineDance\\BeginnerDanceLinks.txt")
    #os.chdir("C:\\Users\\Ethan\\Desktop\\MasterLineDances\\BeginnerLineDances")
    os.chdir(save_path);
    for line in dance_links:
        try:
            #driver = Chrome("/Users/EthanCC/Desktop/LineDance/chromedriver",chrome_options=chrome_options)
            driver.get(line)
            #driver.implicitly_wait(5)
            #time.sleep(1)
            song_title = driver.find_element_by_xpath("//*[@id=\"fullwidth\"]/div[14]")
            song_details = driver.find_element_by_xpath("//*[@id=\"sheetinfo\"]/table/tbody/tr[1]")
            artist = driver.find_element_by_xpath("//*[@id=\"musicinfo\"]")
            steps = driver.find_element_by_xpath("//*[@id=\"fullwidth\"]/table/tbody/tr/td[1]")
            #file_name = os.path.join(save_path, str(song_title.text).replace(" ","").replace("\"\'","").replace('/','-') + "StepSheets.txt")
            file = open(file_name, "w",)
            file.write(str(song_title.text) + ",\n")
            file.write(song_details.text + ",\n\n")
            file.write(artist.text + ",\n")
            file.write(steps.text)
            print("Finished Dance: " + song_title.text)
            file.close()
        except:
            print("Error on link: " + line)


