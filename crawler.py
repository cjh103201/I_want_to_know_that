#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time

from pandas import DataFrame

import re

# 변수  선언
num = [];
name = [];
year = [];
team = [];
position = []

war = []  # 승리기여도
g = []  # 경기수
ts = []  # 타석
ab = []  # 타수
r1 = []  # 득점
h = []  # 안타
b2 = []  # 2루타
b3 = []  # 3루나
hr = []  # 홈런
tb = []  # 루타수
rbi = []  # 타점
sb = []  # 도루 성공
cs = []  # 도루 실패
bb = []  # 볼넷
hbp = []  # 몸에맞는공
bb4 = []  # 고의사구
so = []  # 삼진
gdp = []  # 병살
ht = []  # 희타
hb = []  # 희비
avg = []  # 타율
obp = []  # 출루율
slg = []  # 장타율
ops = []


def addListData(lines):
    # print("in")
    reg = re.compile('([0-9]+)([ㄱ-힣]+)([0-9]{2})([a-zA-Zㄱ-힣])([0-9a-zA-Zㄱ-힣]+)')

    for j in range(0, len(lines) - 1, 28):

        if lines[j].startswith("820") :
            print("aa")

        sp_lines = re.split(reg, lines[j])
        num.append(sp_lines[1])
        name.append(sp_lines[2])
        year.append(sp_lines[3])
        team.append(sp_lines[4])
        if len(sp_lines) < 7  :
            position.append("")
        else :
            position.append(sp_lines[5])

        war.append(lines[j + 1])
        g.append(lines[j + 2])
        ts.append(lines[j + 3])
        ab.append(lines[j + 4])
        r1.append(lines[j + 5])
        h.append(lines[j + 6])
        b2.append(lines[j + 7])
        b3.append(lines[j + 8])
        hr.append(lines[j + 9])
        tb.append(lines[j + 10])
        rbi.append(lines[j + 11])
        sb.append(lines[j + 12])
        cs.append(lines[j + 13])
        bb.append(lines[j + 14])
        hbp.append(lines[j + 15])
        bb4.append(lines[j + 16])
        so.append(lines[j + 17])
        gdp.append(lines[j + 18])
        ht.append(lines[j + 19])
        hb.append(lines[j + 20])
        avg.append(lines[j + 21])
        obp.append(lines[j + 22])
        slg.append(lines[j + 23])
        ops.append(lines[j + 24])


def dataParsing(data):
    non_zero_text = []
    for t in data:
        tbl_txt = t.text
        rows = tbl_txt.split('\n')

        for r in rows:
            if len(r) > 0:
                non_zero_text.append(r)
    for i in range(5, len(non_zero_text), 6):
        l1 = re.split('\s+', non_zero_text[i])
        new_list = []
        for l in l1:
            if len(l) > 0:
                new_list.append(l)
        addListData(new_list)


def getData(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    tbl = soup.select("#mytable")
    return (tbl)


if __name__ == '__main__':

    for k in range(0, 9001, 500):
        print(str(k))
        start = str(k)
        url = "http://www.statiz.co.kr/stat.php?mid=stat&re=0&ys=1982&ye=2019&se=0&te=&tm=&ty=0" \
              "&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=1&o1=WAR_ALL_ADJ&o2=TPA&de=1&lr=0&tr=&cv=&ml=1&sn=500&pa=" + start + "&si=&cn="

        driver = webdriver.Chrome('/Users/jeehyun/Downloads/chromedriver')
        driver.implicitly_wait(10)

        driver.get(url)
        time.sleep(10)
        data500 = getData(driver)
        dataParsing(data500)

        driver.quit()

    df_reglar_season = DataFrame({'num': num, 'name': name, 'year': year, 'team': team, 'position': position,
                                  'war': war, 'g': g, 'ts': ts, 'ab': ab, 'r1': r1, 'h': h, 'b2': b2, 'b3': b3,
                                  'hr': hr, 'tb': tb, 'rbi': rbi, 'sb': sb, 'cs': cs, 'bb': bb, 'hbp': hbp,
                                  'bb4': bb4, 'so': so, 'gdp': gdp, 'ht': ht, 'hb': hb, 'avg': avg, 'obp': obp,
                                  'slg': slg, 'ops': ops})
    df_reglar_season.to_csv("/Users/jeehyun/Downloads/reg_season_all.csv", mode='w')
    print("complete")
