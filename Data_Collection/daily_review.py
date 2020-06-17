# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 21:20:09 2020

@author: Kyoung yeon
"""
# 모듈
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame

total_data = DataFrame()

def data_parsing(html_data) :
    soup_detail = BeautifulSoup(html_detail, 'html.parser')
    print(html_data)

    df_temp = DataFrame()
    return df_temp


if __name__ == "__main__":
    driver = webdriver.Chrome('/Users/jeehyun/Downloads/chromedriver')
    driver.implicitly_wait(10)

    url='https://www.koreabaseball.com/Schedule/Schedule.aspx'
    driver.get(url)
    driver.implicitly_wait(10)

    for year in range(2001, 2002):
        print(year)
        driver.find_element_by_xpath("//select[@id='ddlYear']/option[@value=" + str(year) + "]").click()   # 년 선택
        driver.implicitly_wait(3)

        for month in range(3,5):
            driver.find_element_by_xpath("//select[@id='ddlMonth']/option[@value=" + str(month) + "]").click() # 월 선택
            driver.implicitly_wait(5)

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            tr = soup.select(".relay > a")
            for i in range(0, len(tr)):
                tags = str(tr[i])
                href = tags.split('href="')[1].split('"')[0]

                driver.get('https://www.koreabaseball.com' + href)

                html_detail = driver.page_source
                df_temp_return = data_parsing(html_detail)
                total_data.append(df_temp_return)

    total_data.to_csv("")



batter_record = pd.DataFrame(columns=['date',
                                      'team_self',
                                      'team_match',
                                      'player',
                                      'inn_1',
                                      'inn_2',
                                      'inn_3',
                                      'inn_4',
                                      'inn_5',
                                      'inn_6',
                                      'inn_7',
                                      'inn_8',
                                      'inn_9',
                                      'inn_10',
                                      'inn_11',
                                      'inn_12',
                                      'inn_13',
                                      'inn_14',
                                      'inn_15',
                                      'inn_16',
                                      'inn_17',
                                      'inn_18',
                                      'tasu',
                                      'anta',
                                      'tajum',
                                      'score',
                                      'tayoul'])

# for j in range(2017,2019):
#     print(j)
#                 driver.implicitly_wait(10)
#
#                 html = driver.page_source
#                 soup = BeautifulSoup(html, 'html.parser')
#
#
#
#
#                 # 컬럼목록 1
#                 # for문 변수 생성으로 inning컬럼(리스트형)생성
#                 import sys
#                 mod = sys.modules[__name__]
#
#                 for a in range(1,19):
#                     setattr(mod, 'inn_{}'.format(a), [])
#
#
#
#                 # 컬럼목록 2
#                 date=[]
#                 team_1=[]
#                 team_2=[]
#                 player=[]
#                 tasu=[]
#                 anta=[]
#                 tajum=[]
#                 score=[]
#                 tayoul=[]
#
#                 outlist=[]
#
#
#                 batter_num = len(soup.select('.hitter-record-wrap')[0].find_all('tbody')[-1].select('tr'))
#
#                 # date
#                 datetag = soup.select_one('#lblGameDate').get_text()
#                 date.append(datetag)
#                 for b in range(1,batter_num):
#                     date.append(datetag)
#
#
#                 # team_1,team_2
#                 team1_tag = soup.select_one('#lblAwayHitter').get_text().split(' ')[0]
#                 team_1.append(team1_tag)
#                 for b in range(1,batter_num):
#                     team_1.append(team1_tag)
#
#                 team2_tag = soup.select_one('#lblHomeHitter').get_text().split(' ')[0]
#                 team_2.append(team2_tag)
#                 for b in range(1,batter_num):
#                     team_2.append(team2_tag)
#
#
#
#                 # team_1
#                 for c in range(0,batter_num):
#
#                     # player (선수 명단)
#                     player_tag = soup.select('#tblAwayHitter1')[0].select('tbody')[0].select('tr')[c].select('td')[0].get_text() #김상수
#                     player.append(player_tag)
#
#                     # 타자 기록 1 :inn(이닝)에 따라
#                     record_t = soup.select('#tblAwayHitter2')[0].select('tbody')[0].select('tr')[c] #개인 타자기록 전체
#                     inning = int(soup.select('#tblAwayHitter2')[0].select('thead')[0].select('th')[-1].get_text())#마지막 회
#
#                     inlist=[]
#                     for m in range(0,inning):
#                         if (record_t.select('td')[m].get_text())=='\xa0':
#                             record_tag=''
#                         else:
#                             record_tag = record_t.select('td')[m].get_text()
#                         inlist.append(record_tag)
#                     outlist.append(inlist)
#
#                     df_batter = pd.DataFrame(outlist)
#
#                     # inn컬럼에 넣어주기
#                     for d,e in zip(range(0,inning),range(1,19)):
#                         setattr(mod, 'inn_{}'.format(e), df_batter.iloc[:,d])
#                 outlist=[]
#
#                 # 빈 inn컬럼에 '' 넣어주기
#                 for f in range(10,19):
#                     a = eval('inn_{}'.format(f))
#                     if a == []:
#                         for g in range(0,batter_num):
#                             a.append('')
#
#
#                 # 타자 기록 2 (타수, 안타, 타점, 득점, 타율 )
#                 #soup.select('#tblAwayHitter3')[0].select('thead')[0].select('tr')[0].select('th')[0].get_text()#목록
#
#                 # tasu
#                 for x in range(0,batter_num):
#                     reco2_t = soup.select('#tblAwayHitter3')[0].select('tbody')[0].select('tr')[x].select('td')[0].get_text()
#                     tasu.append(reco2_t)
#
#                 # anta
#                 for x in range(0,batter_num):
#                     reco2_a = soup.select('#tblAwayHitter3')[0].select('tbody')[0].select('tr')[x].select('td')[1].get_text()
#                     anta.append(reco2_a)
#
#                 # tajum
#                 for x in range(0,batter_num):
#                     reco2_tj = soup.select('#tblAwayHitter3')[0].select('tbody')[0].select('tr')[x].select('td')[2].get_text()
#                     tajum.append(reco2_tj)
#
#                 # score
#                 for x in range(0,batter_num):
#                     reco2_sc = soup.select('#tblAwayHitter3')[0].select('tbody')[0].select('tr')[x].select('td')[3].get_text()
#                     score.append(reco2_sc)
#
#                 # tayoul
#                 for x in range(0,batter_num):
#                     reco2_ty = soup.select('#tblAwayHitter3')[0].select('tbody')[0].select('tr')[x].select('td')[4].get_text()
#                     tayoul.append(reco2_ty)
#
#
#                 batter_record_1 = pd.DataFrame({'date':date,
#                                                 'team_self':team_1,
#                                                 'team_match':team_2,
#                                                 'player':player,
#                                                 'inn_1':inn_1,
#                                                 'inn_2':inn_2,
#                                                 'inn_3':inn_3,
#                                                 'inn_4':inn_4,
#                                                 'inn_5':inn_5,
#                                                 'inn_6':inn_6,
#                                                 'inn_7':inn_7,
#                                                 'inn_8':inn_8,
#                                                 'inn_9':inn_9,
#                                                 'inn_10':inn_10,
#                                                 'inn_11':inn_11,
#                                                 'inn_12':inn_12,
#                                                 'inn_13':inn_13,
#                                                 'inn_14':inn_14,
#                                                 'inn_15':inn_15,
#                                                 'inn_16':inn_16,
#                                                 'inn_17':inn_17,
#                                                 'inn_18':inn_18,
#                                                 'tasu':tasu,
#                                                 'anta':anta,
#                                                 'tajum':tajum,
#                                                 'score':score,
#                                                 'tayoul':tayoul
#                                                 })
#                 batter_record = batter_record.append(batter_record_1)
#     #        driver.get('https://www.koreabaseball.com/Schedule/Schedule.aspx')
#     #        driver.find_element_by_xpath("//select[@id='ddlYear']/option[@value="+str(j)+"]").click()
#     #
#
#                 # ---------------------------------------------------------------------------
#                 # team_2 --------------------------------------------------------------------
#                 # ---------------------------------------------------------------------------
#
#                 # 컬럼목록 1
#                 # for문 변수 생성으로 inning컬럼(리스트형)생성
#                 for a in range(1,19):
#                     setattr(mod, 'inn_{}'.format(a), [])
#
#                 date=[]
#                 team_1=[]
#                 team_2=[]
#                 player=[]
#                 tasu=[]
#                 anta=[]
#                 tajum=[]
#                 score=[]
#                 tayoul=[]
#
#                 outlist=[]
#
#
#                 batter_num = len(soup.select('.hitter-record-wrap')[1].find_all('tbody')[-1].select('tr'))
#
#
#                 # date
#                 datetag = soup.select_one('#lblGameDate').get_text()
#                 date.append(datetag)
#                 for w in range(1,batter_num):
#                     date.append(datetag)
#
#
#                 # team_1,team_2
#                 team1_tag = soup.select_one('#lblAwayHitter').get_text().split(' ')[0]
#                 team_1.append(team1_tag)
#                 for w in range(1,batter_num):
#                     team_1.append(team1_tag)
#
#                 team2_tag = soup.select_one('#lblHomeHitter').get_text().split(' ')[0]
#                 team_2.append(team2_tag)
#                 for w in range(1,batter_num):
#                     team_2.append(team2_tag)
#
#
#
#
#                 # team_2
#                 for y in range(0,batter_num):
#
#                     # player (선수 명단)
#                     player_tag = soup.select('#tblHomeHitter1')[0].select('tbody')[0].select('tr')[y].select('td')[0].get_text() #김상수
#                     player.append(player_tag)
#
#                     # 타자 기록 1 :inn(이닝)에 따라
#                     record_t = soup.select('#tblHomeHitter2')[0].select('tbody')[0].select('tr')[y] #개인 타자기록 전체
#                     inning = int(soup.select('#tblHomeHitter2')[0].select('thead')[0].select('th')[-1].get_text())#마지막 회
#
#                     inlist=[]
#                     for m in range(0,inning):
#                         if (record_t.select('td')[m].get_text())=='\xa0':
#                             record_tag=''
#                         else:
#                             record_tag = record_t.select('td')[m].get_text()
#                         inlist.append(record_tag)
#                     outlist.append(inlist)
#
#                     df_batter = pd.DataFrame(outlist)
#
#                     # inn컬럼에 넣어주기
#                     for d,e in zip(range(0,inning),range(1,19)):
#                         setattr(mod, 'inn_{}'.format(e), df_batter.iloc[:,d])
#                 outlist=[]
#
#                 # 빈 inn컬럼에 '' 넣어주기
#                 for f in range(10,19):
#                     a = eval('inn_{}'.format(f))
#                     if a == []:
#                         for g in range(0,batter_num):
#                             a.append('')
#
#
#
#
#                 # 타자 기록 2 (타수, 안타, 타점, 득점, 타율 )
#                 #soup.select('#tblAwayHitter3')[0].select('thead')[0].select('tr')[0].select('th')[0].get_text()#목록
#
#                 # tasu
#                 for x in range(0,batter_num):
#                     reco2_t = soup.select('#tblHomeHitter3')[0].select('tbody')[0].select('tr')[x].select('td')[0].get_text()
#                     tasu.append(reco2_t)
#
#                 # anta
#                 for x in range(0,batter_num):
#                     reco2_a = soup.select('#tblHomeHitter3')[0].select('tbody')[0].select('tr')[x].select('td')[1].get_text()
#                     anta.append(reco2_a)
#
#                 # tajum
#                 for x in range(0,batter_num):
#                     reco2_tj = soup.select('#tblHomeHitter3')[0].select('tbody')[0].select('tr')[x].select('td')[2].get_text()
#                     tajum.append(reco2_tj)
#
#                 # score
#                 for x in range(0,batter_num):
#                     reco2_sc = soup.select('#tblHomeHitter3')[0].select('tbody')[0].select('tr')[x].select('td')[3].get_text()
#                     score.append(reco2_sc)
#
#                 # tayoul
#                 for x in range(0,batter_num):
#                     reco2_ty = soup.select('#tblHomeHitter3')[0].select('tbody')[0].select('tr')[x].select('td')[4].get_text()
#                     tayoul.append(reco2_ty)
#
#
#
#                 batter_record_2 = pd.DataFrame({'date':date,
#                                                 'team_self':team_2,
#                                                 'team_match':team_1,
#                                                 'player':player,
#                                                 'inn_1':inn_1,
#                                                 'inn_2':inn_2,
#                                                 'inn_3':inn_3,
#                                                 'inn_4':inn_4,
#                                                 'inn_5':inn_5,
#                                                 'inn_6':inn_6,
#                                                 'inn_7':inn_7,
#                                                 'inn_8':inn_8,
#                                                 'inn_9':inn_9,
#                                                 'inn_10':inn_10,
#                                                 'inn_11':inn_11,
#                                                 'inn_12':inn_12,
#                                                 'inn_13':inn_13,
#                                                 'inn_14':inn_14,
#                                                 'inn_15':inn_15,
#                                                 'inn_16':inn_16,
#                                                 'inn_17':inn_17,
#                                                 'inn_18':inn_18,
#                                                 'tasu':tasu,
#                                                 'anta':anta,
#                                                 'tajum':tajum,
#                                                 'score':score,
#                                                 'tayoul':tayoul
#                                                 })
#                 batter_record = batter_record.append(batter_record_2)
#
#
#             else:
#                 pass
#
#
#         driver.get('https://www.koreabaseball.com/Schedule/Schedule.aspx')
#         driver.find_element_by_xpath("//select[@id='ddlYear']/option[@value="+str(j)+"]").click()





#driver.find_element_by_class_name("relay").find_element_by_tag_name("a").click()
#
##driver.back()
##driver.back()
#


