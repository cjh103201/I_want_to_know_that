# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:38:49 2020

@author: Kyoung yeon
"""
run profile1

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np



driver = webdriver.Chrome('C:/Users/Lenovo/Downloads/chromedriver_win32/chromedriver.exe')
url='https://www.koreabaseball.com/Schedule/Schedule.aspx'
driver.get(url)
driver.implicitly_wait(5)


gameCenter = pd.DataFrame(columns=['year',
                                   'date',
                                   'playtime',
                                   'playteam_1',
                                   'playteam_2',
                                   'score_1',
                                   'score_2',
                                   'ground'])


for j in range(2001,2021):
    print(j)  
    driver.find_element_by_xpath("//select[@id='ddlYear']/option[@value="+str(j)+"]").click()
    driver.implicitly_wait(3)
    
    
    for k in range(1,13):
        print(k)
        driver.find_element_by_xpath("//select[@id='ddlMonth']/option[@value="+str(k)+"]").click()
        driver.implicitly_wait(3)
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser') 
            
        data_na = soup.select('tr')[1].get_text()
        if data_na == '데이터가 없습니다.':
            continue
        else:
            pass
    
    
        # 컬럼 목록
        year=[j]
        date=[]
        playtime=[]
        playteam_1=[]
        playteam_2=[]
        score_1=[]
        score_2=[]
        ground=[]
   
    
        for i in range(1,len(soup.select('tr'))):
            year.append('')
            # 날짜 컬럼
            daytag = soup.select('tr')[i].select(".day")
            if daytag == []:
                date.append('')
            else:
                daytag = daytag[0].get_text()
                date.append(daytag)
            
            # 시간 컬럼
            timetag = soup.select('tr')[i].select(".time")[0].get_text()
            playtime.append(timetag)
               
            # 팀1,팀2 컬럼
            playteam_tag1 = soup.select('tr')[i].select(".play > span")[0].get_text()
            playteam_tag2 =soup.select('tr')[i].select(".play > span")[1].get_text()
            playteam_1.append(playteam_tag1)
            playteam_2.append(playteam_tag2)
            
            # 점수1, 점수2 컬럼
            score_tag1 = soup.select('tr')[i].select(".play > em")[0].get_text().split('vs')[0]
            score_tag2 = soup.select('tr')[i].select(".play > em")[0].get_text().split('vs')[1]
            score_1.append(score_tag1)
            score_2.append(score_tag2)
                              
            # 구장 컬럼  
            groundtag = soup.select('tr')[i].select('td')[-2:-1][0].get_text()
            ground.append(groundtag)
           
        
        year = year[:-1]
        pages = pd.DataFrame({'year':year,
                              'date':date, 
                              'playtime':playtime,
                              'playteam_1':playteam_1,
                              'playteam_2':playteam_2,
                              'score_1':score_1,
                              'score_2':score_2,
                              'ground':ground})      
        gameCenter = gameCenter.append(pages)    
 
# 파일로 저장    
gameCenter.to_csv('daily_game.csv',encoding='euc-kr')
# encoding='utf-8-sig'
# encoding='cp949'

# 파일 불러오기
dataset = pd.read_csv('daily_game.csv',encoding='cp949')
dataset


