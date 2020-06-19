#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############
# by Jeehyun
# 월별로 나눠진 daily_review 데이터 merge
#############
import pandas as pd
from pandas import DataFrame

df_total_daily_review = DataFrame()

for y in range(2001, 2020):
    for m in range(3, 11):
        filename = "daily_review_" + str(y) + "_" + str(m) + ".csv"
        df_month  = pd.read_csv("../Data/Temp_Data/daily_reviews/"+filename)
        if len(df_month) > 0:
            df_total_daily_review = df_total_daily_review.append(df_month, ignore_index=True)

df_total_daily_review.to_csv("../Data/Final_Data/total_daily_data.csv")

