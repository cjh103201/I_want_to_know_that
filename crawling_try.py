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


url='http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=1982&ye=2018&sn=100&pa'

driver.get(url)
driver.implicitly_wait(10)

html = driver.find_element_by_xpath('//*[@id="mytable"]/tbody').get_attribute("innerHTML") #기록 table을 str형태로 저장
soup = BeautifulSoup(html, 'html.parser') #str 객체를 BeautifulSoup 객체로 변경

temp = [i.text.strip() for i in soup.findAll("tr")] #tr 태그에서, text만 저장하기
temp = pd.Series(temp) #list 객체에서 series 객체로 변경





#'순'이나 'W'로 시작하는 row 제거
# 즉, 선수별 기록만 남기고, index를 reset 해주기
temp = temp[~temp.str.match("[순W]")].reset_index(drop=True) 

temp = temp.apply(lambda x: pd.Series(x.split(' '))) #띄어쓰기 기준으로 나눠서 dataframe으로 변경

#선수 팀 정보 이후 첫번째 기록과는 space 하나로 구분, 그 이후로는 space 두개로 구분이 되어 있음 
#그래서 space 하나로 구분을 시키면, 빈 column들이 존재 하는데, 해당 column들 제거 
temp = temp.replace('', np.nan).dropna(axis=1) 

#WAR 정보가 들어간 column이 2개 있다. (index가 1인 column과, 제일 마지막 column)
#그 중에서 index가 1인 columm 제거 
temp = temp.drop(1, axis=1)

#선수 이름 앞의 숫자 제거
temp[0] = temp[0].str.replace("^\d+", '')

# 선수들의 생일 정보가 담긴 tag들 가지고 오기
birth = [i.find("a") for i in soup.findAll('tr') if 'birth' in i.find('a').attrs['href']]

# tag내에서, 생일 날짜만 추출하기 
p = re.compile("\d{4}\-\d{2}\-\d{2}")
birth = [p.findall(i.attrs['href'])[0] for i in birth]

# 생일 column 추가
temp['생일'] = birth

# page별 완성된 dataframe을 계속해서 result에 추가 시켜주기 
if i == 0:
    result = temp
else:
    result = result.append(temp)
    result = result.reset_index(drop=True)
    
print(i, "완료")
    
    














