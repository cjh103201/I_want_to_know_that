#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############
# by Jeehyun
# 01 ~ 19년까지 경기가 있던 날 / 지역의 날씨 데이터를 하나의 csv 파일로 합침
# (4월1일부터 11월30일까지의 데이터)
#############

import pandas as pd

w_data = pd.read_csv("../Data/weather/2001.csv",  encoding='cp949')

for i in range(2002, 2020):
    filename = "../Data/weather/" + str(i) + ".csv"
    tmp = pd.read_csv(filename, encoding='cp949')
    w_data.append(tmp)

w_data.to_csv("../Data/weather.csv")