#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############
# by Jeehyun
# 날씨 데이터와 일별 경기 데이터를 사용한 모델링
#############
import pandas as pd


# 1. 데이터 읽기
df_dw_game = pd.read_csv("../Data/weather_ground_merge.csv")
df_rs = pd.read_csv("../Data/regular_season_data.csv")

print(df_dw_game)
print(df_rs)

