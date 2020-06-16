# 추가 필요 전처리
import pandas as pd
regular = pd.read_csv('regular_merge.csv')

del regular['Unnamed: 0']    # 불필요컬럼 제거
del regular['batter_name']   # 중복컬럼 제거
del regular['birthday']      # 중복컬럼 제거

year_imsi=[]
for i in regular['year']:
    if i>20:
        year_imsi.append(int('19'+str(i)))
    elif i<10:
        year_imsi.append(int('200'+str(i)))
    else:
        year_imsi.append(int('20'+str(i)))     # 2005 형태로 연도 재가공

regular['year'] = year_imsi   # 가공된 데이터 덮어쓰기
regular['age'] = regular['year'] - regular['birth'].str[:4].astype('int') + 1    # 해당 시즌년도 - 출생년도 + 1 = 해당 시즌 나이

regular['height'] = regular['height'].map(lambda x : int(x.replace('cm','')))   # 키 데이터 숫자형태로 재가공
regular['weight'] = regular['weight'].map(lambda x : int(x.replace('kg','')))   # 몸무게 데이터 숫자형태로 재가공

regular = regular[['name','year','team','position','birth','height','weight','age','war', 'g', 'ts', 'ab', 'r1', 'h', 'b2', 'b3', 'hr', 'tb',
                   'rbi', 'sb', 'cs', 'bb', 'hbp', 'bb4', 'so', 'gdp', 'ht', 'hb', 'avg', 'obp', 'slg', 'ops']]     # 컬럼 순서 변경

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

for i in regular['year']:
    
x_train, x_test, y_train, y_test = train_test_split(regular.iloc[:,5:-3],
                                                    regular.iloc[:,-3],
                                                    random_state=10)
m_rf = RandomForestRegressor()
m_rf.fit(x_train, y_train)
m_rf.score(x_test, y_test)
m_rf.predict(x_test)

regular.iloc[:,5:-3].columns

regular_num=[] ; rf_num=[]
for i in range(len(regular.iloc[:,5:-3].columns)):
    regular_num.append(regular.iloc[:,5:-3].columns[i])
    rf_num.append(m_rf.feature_importances_[i]*100)

df_feature = pd.DataFrame({'feature_name' : regular_num,'feature_importance' : rf_num})

df_feature.sort_values('feature_importance', ascending=False)




