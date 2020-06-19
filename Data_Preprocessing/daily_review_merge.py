#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############
# by Jeehyun
# 월별로 나눠진 daily_review 데이터 merge
#############
import pandas as pd

for y in range(2001, 2020):
    for m in range(3, 11):
        filename = "daily_review_" + str(y) + "_" + str(m) + ".csv"
        df_month  = pd.read_csv("../Data/"+filename)
        print(df_month)
