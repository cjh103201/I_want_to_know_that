# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:38:49 2020

@author: Kyoung yeon
"""
# try!!!!!
run profile1

# matplotlib 한글 출력 가능하도록 만들기
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 데이터 크롤링 모듈
from selenium import webdriver
from bs4 import BeautifulSoup
import re

# 데이터 분석 모듈
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from datetime import datetime

reg = pd.read_csv("C:/Users/Lenovo/Documents/카카오톡 받은 파일/야구/Regular_Season_Batter.csv",encoding='cp949')
reg
reg.head()




driver = webdriver.Chrome('C:/Users/Lenovo/Downloads/chromedriver_win32/chromedriver.exe')


url='https://www.koreabaseball.com/Schedule/Schedule.aspx'

driver.get(url)
driver.implicitly_wait(5)


driver.find_element_by_xpath("//select[@id='ddlYear']/option[@value=2001]").click()
driver.find_element_by_xpath("//select[@id='ddlMonth']/option[@value=04]").click()


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser') #str 객체를 BeautifulSoup 객체로 변경


# 컬럼 목록
dayweek=[]
playtime=[]
playteam_1=[]
playteam_2=[]
score_1=[]
score_2=[]
ground=[]



for i in range(1,len(soup.select('tr'))+1):
    print(i)
    
    # 날짜 컬럼
    daytag = soup.select('tr')[1].select(".day")
      #daytag = soup.select('tr')[2].select(".day")
    
    if daytag == []:
        dayweek.append('')
    else:
        daytag = daytag[0].get_text()
        dayweek.append(daytag)
    
    # 시간 컬럼
    timetag = soup.select('tr')[1].select(".time")[0].get_text()
    playtime.append(timetag)
    
    
    # 팀1,팀2 컬럼
    playteam_tag1 = soup.select('tr')[1].select(".play > span")[0].get_text()
    playteam_tag2 =soup.select('tr')[1].select(".play > span")[1].get_text()
    playteam_1.append(playteam_tag1)
    playteam_2.append(playteam_tag2)
    
    
    # 점수1, 점수2 컬럼
    score_tag1 = soup.select('tr')[1].select(".play > em")[0].get_text().split('vs')[0]
    score_tag2 = soup.select('tr')[1].select(".play > em")[0].get_text().split('vs')[1]
    score_1.append(score_tag1)
    score_2.append(score_tag2)
    
    
    
                 
    # 구장 컬럼  
    groundtag = soup.select('tr')[1].select('td')[-2:-1][0].get_text()
    ground.append(groundtag)
    


# 컬럼 목록 확인    
dayweek
playtime
playteam_1
playteam_2
score_1
score_2
ground
                











