run profile1
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome('chromedriver.exe')

name=[]    # 이름
birth=[]   # 생년월일
height_weight=[]  # 키/몸무게

for i in range(1,1790):
    try:
        url=f'http://www.kbreport.com/player/detail/{i}'
        driver.get(url)
        driver.implicitly_wait(5)
    
        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.content, 'html.parser')
        name.append(soup.select(".player-info-title")[0].get_text().replace('\r\n','').replace('\t',''))     # 이름
        print(soup.select(".player-info-title")[0].get_text().replace('\r\n','').replace('\t',''))
    
        birth.append(soup.select(".player-info-1")[0].get_text())     # 생년월일
        print(soup.select(".player-info-1")[0].get_text())
    
        height_weight.append(soup.select(".player-info-3")[0].get_text())     # 키/몸무게
        print(soup.select(".player-info-3")[0].get_text())
    except:
        i+=1
