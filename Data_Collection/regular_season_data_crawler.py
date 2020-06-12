#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############
# 82년부터 19년까지 정규 시즌 전체 선수별 성적 데이터 크롤링
#############

from selenium import webdriver
from bs4 import BeautifulSoup
import time

import re

import Common.profile1 as p

# 변수  선언
# num = [];
name = []; year = []; team = []; position = []

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

reg = re.compile('([0-9]+)([ㄱ-힣]+)([0-9]{2})([a-zA-Zㄱ-힣])([0-9a-zA-Zㄱ-힣]+)')
reg1 = re.compile('([0-9]+)([ㄱ-힣]+)([0-9]{2})([a-zA-Zㄱ-힣])')
reg2 = re.compile('([ㄱ-힣]+)([0-9]{2})([a-zA-Zㄱ-힣])([0-9a-zA-Zㄱ-힣]+)')
reg3 = re.compile('([ㄱ-힣]+)([0-9]{2})([a-zA-Zㄱ-힣])')

def makeFirstDataParsing(first):
    if re.match(reg, first) :
        sp_lines = re.split(reg, first)

        name.append(sp_lines[2])
        year.append(sp_lines[3])
        team.append(sp_lines[4])
        position.append(sp_lines[5])

    elif re.match(reg1, first) :
        sp_lines = re.split(reg1, first)

        name.append(sp_lines[2])
        year.append(sp_lines[3])
        team.append(sp_lines[4])
        position.append("")

    elif re.match(reg2, first) :
        sp_lines = re.split(reg2, first)
        name.append(sp_lines[1])
        year.append(sp_lines[2])
        team.append(sp_lines[3])
        position.append(sp_lines[4])

    elif re.match(reg3, first) :
        sp_lines = re.split(reg3, first)
        name.append(sp_lines[1])
        year.append(sp_lines[2])
        team.append(sp_lines[3])
        position.append("")


def addListData(lines):
    for idx in range(0, len(lines)-1, 28) :
        makeFirstDataParsing(lines[idx])
        war.append(lines[idx + 1])
        g.append(lines[idx + 2])
        ts.append(lines[idx + 3])
        ab.append(lines[idx + 4])
        r1.append(lines[idx + 5])
        h.append(lines[idx + 6])
        b2.append(lines[idx + 7])
        b3.append(lines[idx + 8])
        hr.append(lines[idx + 9])
        tb.append(lines[idx + 10])
        rbi.append(lines[idx + 11])
        sb.append(lines[idx + 12])
        cs.append(lines[idx + 13])
        bb.append(lines[idx + 14])
        hbp.append(lines[idx + 15])
        bb4.append(lines[idx + 16])
        so.append(lines[idx + 17])
        gdp.append(lines[idx + 18])
        ht.append(lines[idx + 19])
        hb.append(lines[idx + 20])
        avg.append(lines[idx + 21])
        obp.append(lines[idx + 22])
        slg.append(lines[idx + 23])
        ops.append(lines[idx + 24])

def dataParsing(data):
    non_zero_text = []
    for t in data:
        tbl_txt = t.text
        rows = tbl_txt.split('\n')

        for r in rows:
            if len(r) > 0:
                non_zero_text.append(r)

    for i in range(5, len(non_zero_text), 6):
        data = non_zero_text[i].split(" ")

        for d in range(len(data)-1, -1, -1) :
            if len(data[d]) == 0 :
                data[d] = 0
            if (d % 54 != 0 and d%2 == 0):
                del data[d]
        addListData(data)

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

    df_reglar_season = p.DataFrame({'name': name, 'year': year, 'team': team, 'position': position,
                                  'war': war, 'g': g, 'ts': ts, 'ab': ab, 'r1': r1, 'h': h, 'b2': b2, 'b3': b3,
                                  'hr': hr, 'tb': tb, 'rbi': rbi, 'sb': sb, 'cs': cs, 'bb': bb, 'hbp': hbp,
                                  'bb4': bb4, 'so': so, 'gdp': gdp, 'ht': ht, 'hb': hb, 'avg': avg, 'obp': obp,
                                  'slg': slg, 'ops': ops})
    df_reglar_season.to_csv("regular_season_data.csv", mode='w')
    print("complete")
