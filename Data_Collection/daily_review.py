# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 21:20:09 2020

@author: Kyoung yeon
"""
# 모듈
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame, Series

def team_details(s, id):
    selector1 = '#' + id + '1 > tbody > tr > td'
    names_td = s.select(selector1)
    if len(names_td) > 1:
        names = []
        for n in names_td:
            names.append(n.text)

        selector2 = '#' + id +'2 > table > tbody > tr'
        game_details = s.select(selector2)
        if len(game_details) == 0:
            selector2 = '#' + id +'2 > div > div > table > tbody > tr'
            game_details = s.select(selector2)
        game_contents = DataFrame()
        for gd in range(0, len(game_details)):
            soup_tr = BeautifulSoup(str(game_details[gd]), 'html.parser')
            tds = soup_tr.select("td")
            gc = []
            for td in tds:
                gc.append(td.text)
            game_contents = game_contents.append(Series(gc), ignore_index=True)

        selector3 = '#' + id +'3 > tbody > tr'
        game_summary = s.select(selector3)
        game_summaries = DataFrame()
        for gs in range(0, len(game_summary)):
            soup_tr = BeautifulSoup(str(game_summary[gs]), 'html.parser')
            tds = soup_tr.select("td")
            gss = []
            for td in tds:
                gss.append(td.text)
            game_summaries = game_summaries.append(Series(gss), ignore_index=True)
        if len(game_summaries) > 0:
            game_summaries.columns = ['타수', '안타', '타점', '득점', '타율']

        result = game_contents.merge(game_summaries, left_index=True, right_index=True)
        return result
    return DataFrame()


def data_parsing(html_data, total):
    soup_detail = BeautifulSoup(html_detail, 'html.parser')

    # 구장, 관중, 날짜, 개시시간, 경기시간, 팀1, 팀2
    std = soup_detail.select('#txtStadium')[0].text  # 구장
    crd = soup_detail.select('#txtCrowd')[0].text  # 관중
    date = soup_detail.select('#lblGameDate')[0].text  # 날짜
    start = soup_detail.select('#txtStartTime')[0].text  # 개시시간
    runtime = soup_detail.select('#txtRunTime')[0].text  # 경기시간
    team1 = soup_detail.select('#lblAwayHitter')[0].text  # 팀1
    team2 = soup_detail.select('#lblHomeHitter')[0].text  # 팀2

    # 타자별 경기 - team1
    team1_details = team_details(soup_detail, 'tblAwayHitter')

    # 타자별 경기 - team2
    team2_details = team_details(soup_detail, 'tblHomeHitter')

    if len(team1_details) > 0:
        re = pd.concat([team1_details, team2_details])
        total = pd.concat([total, re])

    return total




if __name__ == "__main__":
    total_data = DataFrame()

    for year in range(2001, 2020):
        print(year)

        for month in range(3, 11):
            driver = webdriver.Chrome('../Common/chromedriver')
            driver.implicitly_wait(10)

            url = 'https://www.koreabaseball.com/Schedule/Schedule.aspx'
            driver.get(url)
            driver.implicitly_wait(10)

            driver.find_element_by_xpath("//select[@id='ddlYear']/option[@value=" + str(year) + "]").click()  # 년 선택
            driver.implicitly_wait(3)

            driver.find_element_by_xpath("//select[@id='ddlMonth']/option[@value=" + str(month) + "]").click() # 월 선택
            driver.implicitly_wait(5)

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            tr = soup.select(".relay > a")
            for i in range(0, len(tr)):
                tags = str(tr[i])
                href = tags.split('href="')[1].split('"')[0]

                driver = webdriver.Chrome('/Users/jeehyun/Downloads/chromedriver')
                driver.implicitly_wait(10)
                driver.get('https://www.koreabaseball.com' + href)

                html_detail = driver.page_source
                total_data = data_parsing(html_detail, total_data)
                driver.quit()

    total_data.to_csv("../Data/daily_review.csv", mode='w')


    # total_data.to_csv("")


