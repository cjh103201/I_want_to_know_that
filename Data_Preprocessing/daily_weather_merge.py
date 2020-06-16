#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############
# by Jeehyun
# 날씨 데이터와 일별 경기 데이터 전처리 및 merge
#############

import pandas as pd
from pandas import DataFrame,Series

# 날씨 데이터 읽기
df_wth = pd.read_csv("../Data/weather.csv", encoding="utf8", index_col="Unnamed: 0")

# 지면온도는 nan이 많아서 drop 처리
df_wth = df_wth.drop('지면온도(°C)', axis=1)

# 습도, 강수량의 nan는 0으로 변환
df_wth.iloc[:, 4] = df_wth.iloc[:, 4].fillna(0)
df_wth.iloc[:, 7] = df_wth.iloc[:, 7].fillna(0)

###############

# 일별 경기 내용 읽기 및 전처리
df_dg = pd.read_csv("../Data/daily_game.csv", encoding='cp949')
df_dg = df_dg.drop("Unnamed: 0", axis=1)

# 경기 연도, 날짜 NaN 처리
df_dg.year = df_dg.year.fillna(method="ffill")
df_dg.date = df_dg.date.fillna(method="ffill")
df_dg.year = df_dg.year.astype("int")

# 우천 취소, 경기 예정 등 score값이 nan인 행 drop
df_dg = df_dg.dropna()

# 2020년 이후 데이터 삭제
df_dg = df_dg.loc[df_dg.year != 2020, :]

# 날짜와 시간만 추출해서 날씨 데이터에서 해당 데이터만 추출하기
dates = []
for i in range(0, len(df_dg.year)):
    year = df_dg.iloc[i, 0]
    mm = df_dg.iloc[i, 1][0:2]
    dd = df_dg.iloc[i, 1][3:5]
    time = df_dg.iloc[i, 2][0:3]

    d = str(year) + "-" + str(mm) + "-" + str(dd) + " " + str(time) + "00"
    dates.append(d)

df_dg['dates'] = dates

# ground를 city로 변경
ground_cty_dict = {
    '인천': '인천',
    '수원': '수원',
    '잠실': '서울',
    '시민': '대구',
    '무등': '광주',
    '사직': '부산',
    '대전': '대전',
    '청주': '청주',
    '군산': '군산',
    '제주': '제주',
    '대구': '대구',
    '포항': '포항',
    '광주': '광주',
    '창원': '창원',
    '울산': '울산',
    '마산': '창원',
    '문학': '인천',
    '목동': '서울',
    '고척': '서울'
}

df_dg['city'] = df_dg.ground.apply(lambda x : ground_cty_dict[x])


# city와 dates를 기준으로 데이터 병합
daily_weather_merge = pd.merge(left=df_dg, right=df_wth, how='left', left_on=['dates', 'city'], right_on=['일시', '지점명'])

# 병합된 데이터 전처리
# nan이 있는 컬럼 확인
empty_wth = DataFrame()
for i in range(0, daily_weather_merge.shape[0]):
    if daily_weather_merge.iloc[i,:].isnull().values.any():
        empty_wth = empty_wth.append(daily_weather_merge.iloc[i,:])

empty_wth.to_csv("../Data/emptyWeather.csv")
print(empty_wth)    # nan 데이터 존재하지 않음!
