import pandas as pd
df = pd.read_csv('daily_review_2002_4.csv')
df = df.iloc[:,1:]

df.columns.values[-3:] = ['10','11','12']    # 연장 이닝의 경우 10이닝의 컬럼명이 9로 나와있어서 9이닝과 컬럼명이 겹칠 수 있어 변경필요
df.columns.values[:9] = ['1','2','3','4','5','6','7','8','9']   # 컬럼명 : 이닝

df['구장'] = df['구장'].str[5:]     # 구장 컬럼 재가공(구장이름만 추출)
df['관중'] = df['관중'].str[5:].str.replace(',','').astype('int')     # 관중 컬럼 재가공(관중수만 추출하여 콤마 제거)

df_year = df['날짜'].str.findall('[0-9]').str[:4].str.join('')    # 날짜에서 년도만 추출
df_month = df['날짜'].str.findall('[0-9]').str[4:6].str.join('')  # 날짜에서 월만 추출
df_date = df['날짜'].str.findall('[0-9]').str[6:].str.join('')    # 날짜에서 일만 추출
df_time = df['개시시간'].str[5:9]+'0'    # 개시시간에서 시,분 앞자리(40분이면 4)+0 추출 -> 더블헤더의 경우 실제 개시시간은 14:51분인데 기록상으로 14:50인 경우가 존재함
df['시간'] = pd.to_datetime(df_year + '-' + df_month + '-' + df_date + ' ' + df_time)    # 추출값(str) 모두 결합 후 datetime으로 변환

del df['날짜']
del df['개시시간']
del df['경기시간']

imsi=[]
for i in df['10'].isnull():
    if i == True:
        imsi.append(0)
    else:
        imsi.append(1)

df['연장여부'] = imsi    # 연장 간 경우(10회 이상)=1, 9회까지만 했을 경우=0

dic = {'1땅':'우땅','2땅':'우땅','3땅':'좌땅','유땅':'좌땅','투땅':'중땅','1비':'우플','2비':'우플','3비':'좌플','유비':'좌플','투비':'중땅',
       '1안':'우안','2안':'우안','3안':'좌안','유안':'좌안','투유병':'중병','투2병':'중병','2유병':'우병','유2병':'좌병','32병':'좌병','좌비':'좌플',
       '우비':'우플','중비':'중플','좌희비':'좌플','중희비':'중플','우희비':'우플','1파':'우플','2파':'우플','3파':'좌플','유파':'좌플','4구':'볼넷',
       '좌중안':'좌안','우중안':'우안','좌중2':'좌2','좌중안':'좌안','1번':'우땅','우중2':'우2','우파':'우플','1실':'우땅','우중홈':'우홈','1희번':'우땅',
       '포비':'중땅','포파':'중땅','투희번':'중땅','투실':'중땅','유실':'좌땅','투안':'중안','3직':'좌플','3희번':'좌땅','투직':'중플',
       '좌중홈':'좌홈','3실':'좌땅','2직':'우플','포희번':'중땅','유직':'좌땅','2실':'우땅','좌중3':'좌3','우중3':'우3','좌파':'좌플','좌병':'좌플','고4':'볼넷',
       '유병':'좌병','스낫':'삼진','2병':'우병','포번':'중땅','투번':'중땅','3번':'좌땅','1유병':'우병','포안':'중땅','포땅':'중땅','1직':'우플',
       '투희선':'중땅','좌실':'좌플','투희실':'중땅','야선':'','투포병':'중땅','투파':'중땅','1병':'우병','타방':'볼넷','우희실':'우플','투3병':'중땅',
       '3병':'좌땅','포유병':'중땅'}
# 타구방향을 기준으로 정리함. ex)1땅 = 오른쪽 땅볼이므로 우땅, 1비 = 오른쪽 뜬공이므로 우플

df.iloc[:,:9] = df.iloc[:,:9].applymap(lambda x : x.split('/')[0])     # 한 이닝 2타석 들어선 경우 -> 중2/ 유땅 이런식으로 나옴 -> 재가공 필요(앞에꺼만 추출)
df.iloc[:,:9] = df.iloc[:,:9].apply(lambda x : x.replace(dic))

df['9'].unique()


df_wg = pd.read_csv('Final_Data/weather_ground_merge.csv',encoding='CP949')
df_wg = df_wg.iloc[:,2:]
wg_year = df_wg['year'].astype('str')
wg_month_date = df_wg['date'].str[:2] + '-' + df_wg['date'].str[3:5]
wg_time = df_wg['playtime']

df_wg['date'] = pd.to_datetime(wg_year + '-' + wg_month_date + ' ' + wg_time)

del df_wg['playtime']
del df_wg['dates']
del df_wg['city']


# 인천을 문학으로 변경
ground_imsi=[]
for i in df_wg['ground']:
    if i == '인천':
        ground_imsi.append('문학')
    else:
        ground_imsi.append(i)
df_wg['ground'] = ground_imsi        
    

df_merge = pd.merge(df,df_wg, left_on=['시간','구장'], right_on=['date','ground'])


from datetime import datetime, timedelta
df_merge['시간'][0] + timedelta(days=-1)



df_merge['시간'].unique()
        


