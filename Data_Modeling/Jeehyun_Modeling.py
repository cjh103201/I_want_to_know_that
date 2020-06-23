#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#############
# by Jeehyun
# 날씨 데이터와 일별 경기 데이터를 사용한 모델링
#############
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import MinMaxScaler

# 시각화
import matplotlib.pyplot as plt
import seaborn as sns

# 그래프 한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'AppleGothic'


# 1. 데이터 읽기
df_td = pd.read_csv("../Data/Final_Data/left_right_info_merge.csv", encoding='utf8', index_col='Unnamed: 0')
df_rm = pd.read_csv("../Data/Final_Data/regular_merge.csv", encoding='utf8', index_col='Unnamed: 0')
df_dt = pd.read_csv("../Data/Final_Data/daily_team_data.csv", encoding='cp949', index_col='Unnamed: 0')


# regular_merge.csv 파일 분석
# 데이터
x = df_rm.iloc[:, 5:27]
y = df_rm.ops

x_train, x_test, y_train,y_test = train_test_split(x, y, random_state=0)

# scaling
m_mms = MinMaxScaler()
m_mms.fit(x_train)
x_train_scaled = m_mms.transform(x_train)
x_test_scaled = m_mms.transform(x_test)
x_scaled = m_mms.transform(x)

# LINEAR REGRESSION Model
m_lr  = LinearRegression()
m_lr.fit(x_train_scaled, y_train)

y_predict = m_lr.predict(x_test_scaled)

# plt.scatter(x_test_scaled, y_predict, alpha=0.4)
# plt.show()

m_lr.score(x_test_scaled, y_test)    # 100점

# 회귀계수 및 상수 확인
print(m_lr.coef_)

# 산점도 살펴보기
for i in range(0, x.shape[1]):
    plt.subplot(5,5,i+1)
    plt.scatter(x.iloc[:, i], y, alpha=0.4)
    plt.title(x.columns[i])
plt.show()

# 상관계수
df_scaled = pd.DataFrame(x_scaled)
df_scaled['ops'] = y

cr_scaled = df_scaled.corr(method='pearson')
plt.figure(figsize=(22,22))
sns.heatmap(data=cr_scaled, annot=True, fmt='.2f', linewidths=.5, cmap='RdYlGn_r')
plt.xticks(rotation = - 45 )
plt.yticks(rotation = 45 )
plt.show()

cr_scaled.index = ['height', 'weight', 'age', 'war', 'g', 'ts', 'ab', 'r1', 'h', 'b2',
                     'b3', 'hr', 'tb', 'rbi', 'sb', 'cs', 'bb', 'hbp', 'bb4', 'so', 'gdp', 'ht', 'ops']

cr_scaled.columns = ['height', 'weight', 'age', 'war', 'g', 'ts', 'ab', 'r1', 'h', 'b2',
                     'b3', 'hr', 'tb', 'rbi', 'sb', 'cs', 'bb', 'hbp', 'bb4', 'so', 'gdp', 'ht', 'ops']

ops_cr = cr_scaled.ops
ops_cr.sort_values(ascending=False)  # 상위 5개 





# left_right_merge.csv 파일
df_tdd = pd.read_csv("../Data/Temp_Data/total_daily_data.csv", encoding='utf8', index_col='Unnamed: 0')



df_td = pd.read_csv("../Data/Final_Data/left_right_info_merge.csv", encoding='utf8', index_col='Unnamed: 0')

np.unique(df_td.loc[df_tdd.name == '김태균', 'team1'])

.columns


# 중복 컬럼 제거
del df_td['시간']
del df_td['team1']
del df_td['team2']
del df_td['ground']

# 나눔/드림 데이터 삭제
df_td = df_td.loc[df_td.playteam_1 != '나눔', :]
df_td = df_td.loc[df_td.playteam_1 != '드림', :]

# 히어로즈, 넥섹 -> 키움으로 변경
df_td['playteam_1'] = df_td['playteam_1'].str.replace('히어로즈', '키움')
df_td['playteam_1'] = df_td['playteam_1'].str.replace('넥센', '키움')
df_td['playteam_2'] = df_td['playteam_2'].str.replace('히어로즈', '키움')
df_td['playteam_2'] = df_td['playteam_2'].str.replace('넥센', '키움')

df_td['1루타'] = df_td.loc[:, ['좌안', '중안', '우안']].sum(axis=1)
df_td['2루타'] = df_td.loc[:, ['좌2', '중2', '우2']].sum(axis=1)
df_td['month'] = df_td.date.str[5:7].astype('int')
df_td['time'] = df_td.date.str[11:13]


# 득점, 타율, 홈런, 삼진만
sub_td = df_td.loc[:, ['name', 'playteam_1', '관중', '득점', '타율', '홈런', '삼진', 'year']]


sub_1 = sub_td.loc[:, ['year', 'month', 'time', 'playteam_1', 'playteam_2', '관중', '득점', '안타', '타수', '타율', '타점', '볼넷', '사구', '삼진', 
                       '1루타', '2루타', 'score_1', 'score_2']].groupby(['year', 'month', 'time', 'playteam_1']).sum()

sub_2 = sub_td.loc[:, ['year', 'month', 'time', 'playteam_1', 'playteam_2', '기온(°C)', '강수량(mm)', '풍속(m/s)', '풍향(16방위)', '습도(%)', 
                       'side', 'center', 'fence']].groupby(['year', 'month', 'time', 'playteam_1']).mean()

sub_td2 = pd.merge(sub_1, sub_2,  left_index=True, right_index=True)

# 팀 전체 상관계수 - 히트맵
cor = sub_td2.corr(method='pearson')
plt.figure(figsize=(21,21))
sns.heatmap(data=cor, annot=True, fmt='.2f', linewidths=.5, cmap='RdYlGn_r')
plt.xticks(rotation = - 45 )
plt.yticks(rotation = 45 )
plt.title("팀 전체에 대한 변수 간 상관계수")
plt.show()


# 팀별 상관계수 - 히트맵
teams = list(np.unique(sub_td.playteam_1))      # 팀 목록
for t in range(0, len(teams)):
    tmp = sub_td2.xs(teams[t], level=3)
    tmp_cor = tmp.corr(method='pearson')   
    plt.figure(figsize=(21,21))
    sns.heatmap(data=tmp_cor, annot=True, fmt='.2f', linewidths=.5, cmap='RdYlGn_r')
    plt.xticks(rotation = - 45 )
    plt.yticks(rotation = 45 )
    plt.title(teams[t] + "의 변수 간 상관계수")
    plt.show()

# 팀별 연도별 상관계수 - 선 그래프
# 값을 0-1사이로 scaling
sub_11 = sub_td.loc[:, ['year', 'playteam_1', 'playteam_2', '관중', '득점', '안타', '타수', '타율', '타점', '볼넷', '사구', '삼진', 
                       '1루타', '2루타', 'score_1', 'score_2']].groupby(['year', 'playteam_1']).sum()

sub_22 = sub_td.loc[:, ['year', 'playteam_1', 'playteam_2', '기온(°C)', '강수량(mm)', '풍속(m/s)', '풍향(16방위)', '습도(%)', 
                       'side', 'center', 'fence']].groupby(['year', 'playteam_1']).mean()

sub_td22 = pd.merge(sub_11, sub_22,  left_index=True, right_index=True)

# scaling -> 관중 수와 이외의 변수들의 범위 간격이 크기 때문에 scaling 진행
m_mms = MinMaxScaler()
m_mms.fit(sub_td22)
sub_td22_scaled = pd.DataFrame(m_mms.transform(sub_td22))
sub_td22_scaled.index = sub_td22.index
sub_td22_scaled.columns = list(sub_td22.columns)


# 한화, 롯데, 기아
# KT, 키움
team = '한화'
team = '롯데'
team = 'KIA'
team = 'KT'
team = '키움'

sub2 = sub_td22_scaled.loc[:, ['관중', '득점', '안타', '타수', '타율', '타점', '볼넷', '삼진', '1루타', '2루타']]
cols = list(sub2.columns)

for i in range(1, len(cols)):
    plt.subplot(3,3,i)
    sub2.xs(team, level=1).loc[:,'관중'].plot(color='g')
    sub2.xs(team, level=1).loc[:,cols[i]].plot(color='orange')
    plt.legend()
    plt.show()
plt.suptitle(team)






#
#
# f, a = plt.subplots(3,1)
# sub_td2_scaled.xs('KIA', level=3).xs(2001).plot(kind='bar',ax=a[0])
# sub_td2_scaled.xs('KIA', level=3).xs('2002').plot(kind='bar',ax=a[1])
# sub_td2_scaled.xs('KIA', level=3).xs('2003').plot(kind='bar',ax=a[2])
#
#
# sub_td2_scaled.index[[0]]
#
# plt.bar(index, tips_sum_by_day)
#
# plt.title('Sum of Tips by Day', fontsize=20)
#
# plt.xlabel('Day', fontsize=18)
#
# plt.ylabel('Sum of Tips', fontsize=18)
#
# plt.xticks(index, label, fontsize=15)
#
# plt.show()
#
#
#
#
# sub_td2.xs('KIA', level=3).loc[:,'안타'].plot()
#
#
#
#
# 교통사고df['발생건수'].plot(color='#ff0000')
#
# plt.plot(sub_td2.index, sub_td2.관중, marker='o', color='g')
#
#
# sub_td2.index
#
# for t in range(0, len(teams)):
#     tmp = sub_td2.xs(teams[t], level=3)
#     tmp_cor = tmp.corr(method='pearson')
# #    plt.subplot(4,3,t+1)
#     sns.heatmap(data=tmp_cor, annot=True, fmt='.2f', linewidths=.5, cmap='RdYlGn_r')
#     plt.xticks(rotation = - 45 )
#     plt.yticks(rotation = 45 )
#     plt.title(teams[t] + " 변수 간 상관계수")
#     plt.show()
#
#
#
#
#
# tmp = sub_td2.xs('KIA', level=3)
# tmp.corr(method='pearson')
#
# df_td.columns
#
# ['관중', '득점', '안타', '타수', '타율', '타점', '볼넷', '사구', '삼진', '1루타', '2루타',
#        '연장여부', 'score_1', 'score_2', '기온(°C)', '강수량(mm)', '풍속(m/s)',
#        '풍향(16방위)', '습도(%)', 'side', 'center', 'fence']
#
# sub_td2.unstack()


#
#
# # 원-핫 인코딩 -> 모든 컬럼에 대해
# for i in range(5, x.shape[1]+1):
#     obs = df_rm.iloc[:, i]
#     e = LabelEncoder()
#     e.fit(obs)
#     df_rm.iloc[:, i] = e.transform(obs)
#
# # 변수 중요도 -> RFE
#
# m_rf = rf()
# m_fs = RFE(m_rf, n_features_to_select=15)
# m_fs.fit(x, y)
# m_fs.get_support()
# m_fs.ranking_
#
# # 먼저 변수 중요도  -> 그리고 중요변수 위주로 세부 내용에 대한 분석
#
# # 한화 선수 추출
# df_eagles = df_td.loc[df_td.team1 == '한화', :]
#
# # 한글이 있는  컬럼 : name, team1, team2, 구장, ground
# # 한글을 숫자로 변경하기
# e = LabelEncoder()
# e.fit(df_eagles.name)
# df_eagles['name1'] = e.transform(df_eagles.name)
#
# e = LabelEncoder()
# e.fit(df_eagles.team1.astype(str))
# df_eagles.team1 = e.transform(df_eagles.team1.astype(str))
#
# e = LabelEncoder()
# e.fit(df_eagles.team2.astype(str))
# df_eagles.team2 = e.transform(df_eagles.team2.astype(str))
#
# e = LabelEncoder()
# e.fit(df_eagles.loc[:, '구장'])
# df_eagles.구장 = e.transform(df_eagles.구장)
#
# # 날짜에서 달만 추출
# df_eagles['month'] = df_eagles.date.str[5:7].astype('int')
# del df_eagles['date']
#
# # 유사항목 합치기
# df_eagles['땅볼'] = df_eagles.iloc[:, 40:43].sum(axis=1)
# df_eagles['플라이'] = df_eagles.iloc[:, 43:46].sum(axis=1)
# df_eagles['안타'] = df_eagles.iloc[:, 46:49].sum(axis=1)
# df_eagles['2루타'] = df_eagles.iloc[:, 49:52].sum(axis=1)
# df_eagles['3루타'] = df_eagles.iloc[:, 52:55].sum(axis=1)
# df_eagles['병살'] = df_eagles.iloc[:, 55:57].sum(axis=1)
# df_eagles['홈런'] = df_eagles.iloc[:, 57:60].sum(axis=1)
#
# df_eagles['구장크기평균'] = df_td.loc[:, ['side', 'center', 'fence']].mean(axis=1)
#
# tmp = df_eagles.loc[:, ['team2', '관중', '구장', '득점', '안타', '타수', '타율', '타점', '연장여부',
#               'year', 'score_1', 'score_2', '기온(°C)', '강수량(mm)', '풍속(m/s)',
#               '풍향(16방위)', '습도(%)', '구장크기평균', '볼넷', '사구', '삼진',
#               'name1', 'month', '2루타', '홈런', '땅볼', '플라이', '3루타', '병살']]
#
#
# # 상관관계
# cr = tmp.corr(method='pearson')
# plt.figure(figsize=(29,29))
# sns.heatmap(data=cr, annot=True, fmt='.2f', linewidths=.5, cmap='RdYlGn_r')
# plt.xticks(rotation = - 45 )
# plt.yticks(rotation = 45 )
# plt.show()
#
# df_eagles.groupby('name1')
#
# # 월별 홈런,  안타, 볼넷, 타점 평균
# month_mean = df_eagles.loc[:, ['year', 'month', '홈런', '안타', '볼넷', '타점']].groupby(['year', 'month']).sum()
# month_mean2 = df_eagles.loc[:, ['year', 'month', '기온(°C)', '강수량(mm)', '풍속(m/s)', '풍향(16방위)', '습도(%)']].groupby(['year', 'month']).mean()
#
# month_mean = month_mean.fillna(0)
# month_mean2 = month_mean2.fillna(0)
#
# month_mean.unstack()
#
# for i in range(2001, 2020):
#
#
#
# plt.plot(month_mean.index, month_mean['홈런'], marker='s')
# plt.plot(month_mean.index, month_mean2['기온(°C)'], marker='s', color='g')
# plt.plot(month_mean.index, month_mean2['강수량(mm)'], marker='s', color='b')
# plt.plot(month_mean.index, month_mean2['습도(%)'], marker='s', color='y')
# plt.plot(month_mean.index, month_mean['안타'], marker='s', color='r')
# plt.legend()
# plt.show()
#
#
#
# # 산점도
# plt.scatter(df_td.iloc[:, 19:], df_td.iloc[:, 19:])
# plt.show()
#
#
# print(df_td)
# print(df_rm)
# print(df_dt)
#
# df_td.iloc[:, 19:].shape


# print(df_dt.dates.drop_duplicates().sort_values())


# corr = df_dt.corr(method='pearson')
# print(corr.shape)
#
#
# plt.figure(figsize=(28,28))
# sns.heatmap(data=corr, annot=True, fmt='.2f', linewidths=.5, cmap='RdYlGn_r')
# plt.xticks(rotation = - 45 )
# plt.yticks(rotation = 45 )
# plt.show()

#
#
#
# # 컬럼명 한글로 바꾸기
# # df_rm.columns
# df_rm.columns = ['이름', '년도', '소속팀', '포지션',  '생년월일', '키', '몸무게', '나이', '승리기여도',
#                   '경기수', '타석', '타수', '득점', '안타', '2루타', '3루타', '홈런', '루타수', '타점', '도루성공',
#                   '도루실패', '볼넷', '사구', '고의사구', '삼진', '병살', '희타', '희비', '타율', '출루율', '장타율', 'OPS']
#
# # 2. regular data 상관계수 & 히트맵
# cr = df_rm.iloc[:, 1:].corr(method='pearson')
#
# # 한글 깨짐 방지
# # plt.rcParams['axes.unicode_minus'] = False
# # plt.rcParams['font.family'] = 'AppleGothic'
# #
# # plt.figure(figsize=(28,28))
# # sns.heatmap(data=cr, annot=True, fmt='.2f', linewidths=.5, cmap='RdYlGn_r')
# # plt.xticks(rotation = - 45 )
# # plt.yticks(rotation = 45 )
# # plt.show()
#
#
# # 2. data split
# x =  df_rm.loc[:, ['년도', '키', '몸무게', '나이', '승리기여도',
#                   '경기수', '타석', '타수', '득점', '안타', '2루타', '3루타', '홈런', '루타수', '타점', '도루성공',
#                   '도루실패', '볼넷', '사구', '고의사구', '삼진', '병살', '희타', '희비', '타율', '출루율', '장타율']]
# y = df_rm.OPS
# x_train, x_test,  y_train, y_test = train_test_split(x, y, random_state=0)
#
# # 3. scaling
#
# # 4. interaction
#
# # 5. rf
# m_rf = rf_r()
# m_rf.fit(x_train, y_train)
#
# print(m_rf.score(x_test, y_test))
#
# # 6.
#
#
#
# # 3. ops와 키 / 몸무게 / 나이 등 각자 line 그래프
#
#
# # print(df_td)
# # print(df_rm)
# # print(df_dt)
