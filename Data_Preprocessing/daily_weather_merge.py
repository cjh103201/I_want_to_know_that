#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############
# by Jeehyun
# 날씨 데이터와 일별 경기 데이터 전처리 및 merge
#############

import pandas as pd
from numpy import nan as NA

df_wth = pd.read_csv("../Data/weather.csv", encoding="utf8", index_col="Unnamed: 0")
print(df_wth)

# # nan이 있는 컬럼 확인
# for i in range(0, len(df_wth.columns)):
#     if df_wth.iloc[:, i].isnull().values.any() :
#         print(str(i) + "번째 컬럼 = " + df_wth.columns[i])   # 강수량 / 지면온도
#
# # 지면온도는 drop, 강수량은 0으로 nan처리
# df_wth = df_wth.drop('지면온도(°C)', axis=1)
# df_wth = df_wth.fillna(0)
#
#
# # 경기 내용 파일 읽기 및 전처리
# df_dg = pd.read_csv("../Data/daily_game.csv", encoding='cp949')
# df_dg = df_dg.drop("Unnamed: 0", axis=1)
#
# df_dg.year = df_dg.year.fillna(method="ffill")
# df_dg.date = df_dg.date.fillna(method="ffill")
# df_dg.year = df_dg.year.astype("int")
#
# df_dg = df_dg.dropna()
#
# dates = []
# for i in range(0, len(df_dg.year)):
#     year = df_dg.iloc[i, 0]
#     mm = df_dg.iloc[i, 1][0:2]
#     dd = df_dg.iloc[i, 1][3:5]
#     time = df_dg.iloc[i, 2][0, 3]
#
#     d = year + "-" + mm + "-" + dd + " " + time + "00"
#     dates.append(d)
#
# df_dg["dates"] = dates
#
# ground_cty_dict = {
#     '잠실' : '서울',
#     '시민' : '대구',
#     '무등' : '광주',
#     '사직' : '부산',
#     '마산' : '창원',
#     '문학' : '인천',
#     '목동' : '서울',
#     '고척' : '서울'
# }






# df_dg.year
# print(df_dg.date.str[0:2])
# print(df_dg.date.str[3:5])
# print(df_dg.playtime.str[0:3])
#
#
# def make_data_format(year, date, time):
#     print(year + "-" + date[0:2] + "-" + date[3:5] + " " + time[0:3] + "00")
#
#
#
#
# df_dg.year.apply(make_data_format, df_dg.date, df_dg.playtime)
#
# print(df_dg.year.apply(make_data_format, df_dg.date, df_dg.playtime))

# print(df_dg)
# print(df_wth)

#         지점 지점명                일시  기온(°C)  강수량(mm)  풍속(m/s)  풍향(16방위)  습도(%)
# 0      108  서울  2001-04-01 01:00     3.1      0.0      2.8       270     55
# 1      108  서울  2001-04-01 02:00     3.0      0.0      3.2       270     56
