import csv
import enum
from bs4 import BeautifulSoup
import time
from selenium import webdriver
startURL = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome('C:/Users/Minho/Downloads/chromedriver_win32/chromedriver')
browser.get(startURL)
time.sleep(10)
planetdata=[]
def scrapData():
    for a in range(1,5):
        soup = BeautifulSoup(browser.page_source,'html.parser')
        allul = soup.find_all('ul',attrs={'class','expoplanet'})
        for eachul in allul:
            allLi = eachul.find_all('li')
            temlist = []
            for index, eachli in enumerate(allLi):
                if index==0:
                    temlist.append(eachli.find_all('a')[0].contents[0])
                else:
                    temlist.append(eachli.contents[0])
            planetdata.append(temlist)
        browser.find_element("xpath",'/html/body/div[2]/div/div[3]/section[2]/div/section[2]/div/div/article/div/div[2]/footer/div/div/div/nav/span[2]/a').click()

    with open('scraper.csv','w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(planetdata)
scrapData()