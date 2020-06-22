run profile1
import pandas as pd
import seaborn as sns

daily = pd.read_csv('Final_Data/left_right_info_merge.csv')
del daily['Unnamed: 0']

# 김현수의 성적
hs_score = daily.loc[daily['name'] == '김현수',:]

hs_score[['좌측타구','중간타구','우측타구']].sum()     # 좌측타구:1177, 중간타구:791, 우측타구:1601

hs_score[['좌병','중병','우병']].sum()     # 좌병:0, 중병:4, 우병:61
hs_score[['좌땅','중땅','우땅']].sum()     # 좌땅:254, 중땅:106, 우땅:748
hs_score[['좌플','중플','우플']].sum()     # 좌플:545, 중플:326, 우플:230

hs_score[['좌안','좌2','좌3','좌홈']].sum()     # 좌안:221, 좌2:118, 좌3:8, 좌홈:31
hs_score[['중안','중2','중3','중홈']].sum()     # 중안:309, 중2:23, 중3:0, 중홈:23
hs_score[['우안','우2','우3','우홈']].sum()     # 우안:369, 우2:94, 우3:12, 우홈:87

daily['비 유무'] = [0 if i <= 3 else 1 for i in daily['강수량(mm)']]

sns.barplot(x='비 유무', y='좌측타구', data=hs_score)

def dir_rain(name,direction):
    imsi = daily.loc[daily['name'] == name,:]
    sns.barplot(x='비 유무', y=direction, data=imsi)

dir_rain('김현수','우병')

hs_score['기온(°C)']


sns.barplot(data=hs_score, x='우측타구', y='우안', hue='비 유무')

hs_score.corr() > 0.5
scatter(hs_score)

plt.scatter(x=hs_score['기온(°C)'], y=hs_score['우측타구'])


# import matplotlib
# from matplotlib import rc, font_manager
# import numpy as np
# matplotlib.rcParams['axes.unicode_minus'] = False     # 마이너스 폰트 깨짐현상 수정
# rc('font',family='NanumGothic')

plt.rcParams['font.family'] = 'Malgun Gothic'


####
# regular
regular = pd.read_csv('Final_Data/regular_merge.csv')
rank = pd.read_csv('Temp_Data/teamrank.csv')

regular_merge = pd.merge(regular, rank, left_on=['year','team'], right_on=['연도','팀'])

regular_merge.loc[regular_merge['name'] == '이용규',:].corr()['순']   # 팀 순위와 sb,hbp,hb는 강한 음의 상관관계 -> 출루를 많이 할수록(안타 제외) 팀 순위는 낮아진다(=상위권으로 간다)
sns.heatmap(data=regular_merge.loc[regular_merge['name'] == '이용규',:].corr(), annot=True, fmt='.2f', linewidths=.5, cmap='Blues')


regular_merge = regular_merge[['name','year','team','순','승','무','패','승차','승률','war','g','ts','ab','r1','h','b2','b3','hr','tb','rbi','sb','cs','bb','hbp','bb4',
               'so','gdp','ht','hb','avg','obp','slg','ops']]     # 필요한 컬럼만 추출

def corr_rank(name):
    return regular_merge.loc[regular_merge['name'] == name,:].corr()['순']
    
corr_rank('이성열')

