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

def get_more_info(data_str, length):
    data_list = []
    for i in range(0, length):
        data_list.append(str(data_str))
    return data_list

def data_parsing(html_data, total):
    soup_detail = BeautifulSoup(html_detail, 'html.parser')

    # 구장, 관중, 날짜, 개시시간, 경기시간, 팀1, 팀2
    std = soup_detail.select('#txtStadium')[0].text  # 구장
    crd = soup_detail.select('#txtCrowd')[0].text    # 관중
    date = soup_detail.select('#lblGameDate')[0].text  # 날짜
    start = soup_detail.select('#txtStartTime')[0].text  # 개시시간
    runtime = soup_detail.select('#txtRunTime')[0].text  # 경기시간
    team1 = soup_detail.select('#lblAwayHitter')[0].text.split(' ')[0]  # 팀1
    team2 = soup_detail.select('#lblHomeHitter')[0].text.split(' ')[0]  # 팀2

    # 타자별 경기 - team1
    team1_details = team_details(soup_detail, 'tblAwayHitter')

    # 타자별 경기 - team2
    team2_details = team_details(soup_detail, 'tblHomeHitter')

    if len(team1_details) > 0:
        stds = get_more_info(std, len(team1_details))
        crds = get_more_info(crd, len(team1_details))
        dates = get_more_info(date, len(team1_details))
        starts = get_more_info(start, len(team1_details))
        runtimes = get_more_info(runtime, len(team1_details))
        team1s = get_more_info(team1, len(team1_details))
        team2s = get_more_info(team2, len(team1_details))

        team1_details['구장'] = stds
        team1_details['관중'] = crds
        team1_details['날짜'] = dates
        team1_details['개시시간'] = starts
        team1_details['경기시간'] = runtimes
        team1_details['team1'] = team1s
        team1_details['team2'] = team2s

        stds = get_more_info(std, len(team2_details))
        crds = get_more_info(crd, len(team2_details))
        dates = get_more_info(date, len(team2_details))
        starts = get_more_info(start, len(team2_details))
        runtimes = get_more_info(runtime, len(team2_details))
        team1s = get_more_info(team1, len(team2_details))
        team2s = get_more_info(team2, len(team2_details))

        team2_details['구장'] = stds
        team2_details['관중'] = crds
        team2_details['날짜'] = dates
        team2_details['개시시간'] = starts
        team2_details['경기시간'] = runtimes
        team2_details['team1'] = team2s
        team2_details['team2'] = team1s

        re = pd.concat([team1_details, team2_details])
        total = pd.concat([total, re])

    return total




if __name__ == "__main__":


    for year in range(2001, 2020):
        total_data = DataFrame()
        print(year)

        for month in range(3, 11):
            driver = webdriver.Chrome('../Common/chromedriver')
            driver.implicitly_wait(10)

            url = 'https://www.koreabaseball.com/Schedule/Schedule.aspx'
            driver.get(url)
            driver.implicitly_wait(5)

            driver.find_element_by_xpath("//select[@id='ddlYear']/option[@value=" + str(year) + "]").click()  # 년 선택
            driver.implicitly_wait(5)

            driver.find_element_by_xpath("//select[@id='ddlMonth']/option[@value=" + str(month) + "]").click() # 월 선택
            driver.implicitly_wait(10)

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            tr = soup.select(".relay > a")
            for i in range(0, len(tr)):
                tags = str(tr[i])
                href = tags.split('href="')[1].split('"')[0]

                driver = webdriver.Chrome('/Users/jeehyun/Downloads/chromedriver')
                driver.implicitly_wait(5)
                driver.get('https://www.koreabaseball.com' + href)

                html_detail = driver.page_source
                total_data = data_parsing(html_detail, total_data)

                driver.quit()
        total_data.to_csv("../Data/daily_review_" + year + ".csv", mode='w')

