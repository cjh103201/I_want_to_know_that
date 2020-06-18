import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

regular = pd.read_csv('Final_Data/regular_merge.csv')
teamrank = pd.read_csv('Temp_Data/teamrank.csv')

regular_teamrank_merge = pd.merge(regular,teamrank, left_on=['team','year'], right_on=['팀','연도'])
del regular_teamrank_merge['연도']
del regular_teamrank_merge['팀']


def player_team_corr(player,team):
    imsi = regular_teamrank_merge.loc[(regular_teamrank_merge['name'] == player) & (regular_teamrank_merge['team'] == team),:]
    return imsi.iloc[:,8:34].corr()['순'][:-1]

plt.bar(player_team_corr('이용규','한화').index, player_team_corr('이용규','한화').values)





