###
# 타율,득점,안타,1,2,3루타,홈런,타점,도루성공,도루실패,볼넷,몸에맞는공,삼진 등..
# 1루타 = 안타 - (1,2,3루타) 추가 필요
# 순장타율 = 장타율 - 타율 (순수하게 장타)
# 순출루율 = 출루율 - 타율 (안타가 아닌 볼넷으로 출루한 경우 -> 선구안)



#run profile1

pre_season = pd.read_csv('Pre_Season_Batter.csv', engine='python')
regular_season = pd.read_csv('Regular_Season_batter.csv', engine='python')
regular_season_day = pd.read_csv('Regular_Season_Batter_Day_by_Day_b4.csv', engine='python')

pre_season['AB'].mean()                              # 프리시즌 평균 타석 = 19
pre_season = pre_season[pre_season['AB'] > 20]       # 20타석 이하 데이터 제거

pre_season['height'] = pre_season['height/weight'].str.split('/').str[0].str.replace('cm','').astype('int')     # height/weight 컬럼에서 height 분리
pre_season['weight'] = pre_season['height/weight'].str.split('/').str[1].str.replace('kg','').astype('int')     # height/weight 컬럼에서 weight 분리
del pre_season['height/weight']    # height/weight 컬럼 제거

born_all = pre_season['year_born'].str.findall('[0-9]*').str.join('')         # 생년월일(1995년 12월 14일)을 숫자형태(19951214)로 바꾸기
born = born_all.str[:4] + '-' + born_all.str[4:6] + '-' + born_all.str[6:]    # 숫자형태(19951214)를 1995-12-14 형태로 바꾸기
born = pd.to_datetime(born,format='%Y-%m-%d')     # 1995-12-14 형태를 날짜로 변환
pre_season['birthday'] = born    # 생년월일 컬럼 추가

maan = pd.to_datetime(pre_season['year'].astype('str') + '-01-01') - born     # 당시 시즌 - 생년월일 계산
pre_season = pre_season.reset_index(drop=True)    # 나이 컬럼 생성을 위해 인덱스 초기화(인덱스를 순서대로 재배치)
pre_season['age'] = Series([i.days for i in (maan / 365)])   # 그때당시 나이로 계산


regular_season = regular_season[regular_season['AB'] > 30]                           # 정규시즌 30타석 이하 제거
regular_season = regular_season.loc[regular_season['height/weight'].notnull(),:]     # height/weight이 결측치인 경우 제거
regular_season = regular_season.loc[regular_season['starting_salary'].notnull(),:]   # salary가 결측치인 경우 제거

regular_season['height'] = regular_season['height/weight'].str.split('/').str[0].str.replace('cm','').astype('int')    # height/weight 컬럼에서 height 분리
regular_season['weight'] = regular_season['height/weight'].str.split('/').str[1].str.replace('kg','').astype('int')    # height/weight 컬럼에서 weight 분리
del regular_season['height/weight']   # height/weight 컬럼 제거

regular_season = regular_season.reset_index(drop=True)
r_born_all = regular_season['year_born'].str.findall('[0-9]*').str.join('')            # 생년월일(1995년 12월 14일)을 숫자형태(19951214)로 바꾸기
r_born = r_born_all.str[:4] + '-' + r_born_all.str[4:6] + '-' + r_born_all.str[6:]     # 숫자형태(19951214)를 1995-12-14 형태로 바꾸기
r_born = pd.to_datetime(r_born,format='%Y-%m-%d')     # 1995-12-14 형태를 날짜로 변환
regular_season['birthday'] = r_born                   # 생년월일 컬럼 추가

maan1 = pd.to_datetime(regular_season['year'].astype('str') + '-01-01') - r_born    # 당시 시즌 - 생년월일 계산
regular_season['age'] = Series([i.days for i in (maan1 / 365)])
