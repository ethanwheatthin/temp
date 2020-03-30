from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    driver = webdriver.Chrome("/Users/EthanCC/django-app-test/testapp/chromedriver")
    #driver.get("https://www.copperknob.co.uk/search.aspx?Order=Alphabetical&Lang=en&SearchType=Title&Level=Beginner&Beat=-1&Wall=-1&Search=&recnum=20")

    #driver.get("https://www.copperknob.co.uk/search.aspx?Order=Alphabetical&Lang=en&SearchType=Title&Level=Beginner&Beat=-1&Wall=-1&Search=&recnum=0")
    #title = driver.find_elements_by_xpath("//a[@href]")


    danceFile = open("AdvancedDanceLinks.txt",'a')
    counter = 0
    for i in range(200000):
        try:
            link = "https://www.copperknob.co.uk/search.aspx?Order=Alphabetical&Lang=en&SearchType=Title&Level=Advanced&Beat=-1&Wall=-1&Search=&recnum=" + str(counter)
            driver.get(link)
            driver.implicitly_wait(5000)
            title = driver.find_elements_by_xpath("//a[@href]")
            for elem in title:
                if "/stepsheets/" in elem.get_attribute("href"):
                    danceFile.write(str(elem.get_attribute("href")) + "\n")
                    print(str(i)+" Finished dance: " + str(elem.get_attribute("href")))
            print("Finished page: " + link)
            counter += 20
        except:
            print("Error")
            break
