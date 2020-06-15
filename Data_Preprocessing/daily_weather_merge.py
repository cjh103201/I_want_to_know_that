#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############
# by Jeehyun
# 날씨 데이터와 일별 경기 데이터 merge 및 전처리
#############

import pandas as pd
from numpy import nan as NA

df_wth = pd.read_csv("../Data/weather.csv", encoding="utf8", index_col="Unnamed: 0")

# nan이 있는 컬럼 확인
for i in range(0, len(df_wth.columns)):
    if df_wth.iloc[:, i].isnull().values.any() :
        print(str(i) + "번째 컬럼 = " + df_wth.columns[i])   # 강수량 / 지면온도

# 지면온도는 drop, 강수량은 0으로 nan처리
df_wth = df_wth.drop('지면온도(°C)', axis=1)
df_wth = df_wth.fillna(0)


# 경기 내용 파일 읽기


