from selenium import webdriver
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome('chromedriver.exe')

name=[]    # 이름
birth=[]   # 생년월일
height_weight=[]  # 키/몸무게
i_list = [840,841,842,859,868,869,882,883,889,893,909,913,915,916,917,921,922,923,924,925,926,927,942,943,951,957,961,1004,1036,1054,1057,1335,1373]     # 오류번호 리스트(제외대상)

for i in range(1,1790):
    if i not in i_list:
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

        
birth = [i.split(' ')[1] for i in birth]    # 생년월일 1995-12-14 에서 뒤에꺼만 추출
birth = pd.to_datetime(birth)
height_weight = [i.split(' ')[1] for i in height_weight]    # 000cm/00kg 만 추출
height = [i.split('/')[0] for i in height_weight]    # 키 추출
weight = [i.split('/')[1] for i in height_weight]    # 몸무게 추출


info = DataFrame({'name':name,
                  'birth':birth,
                  'height':height,
                  'weight':weight})

len(info.name.unique())   # 1661 (데이터프레임 길이는 1756으로 겹치는게 95개 존재)
info.loc[info.name == '고우석',:]     # 동명이인 존재

info
