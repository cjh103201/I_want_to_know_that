birth = [i.split(' ')[1] for i in birth]    # 생년월일 1995-12-14 에서 뒤에꺼만 추출
birth = pd.to_datetime(birth)
height_weight = [i.split(' ')[1] for i in height_weight]    # 000cm/00kg 만 추출
height = [i.split('/')[0] for i in height_weight]    # 키 추출
weight = [i.split('/')[1] for i in height_weight]    # 몸무게 추출
team = [i.split(' ')[1] for i in team]      # 팀 추출

(datetime.today() - info['birthday'])/365     # (현재 - 생년월일) / 365 -> 나이 생성하기위해
age = [i.days for i in (datetime.today() - info['birthday'])/365]    # 나이 생성

info = pd.DataFrame({'batter_name':name,
                     'team':team,
                     'birthday':birth,
                     'height':height,
                     'weight':weight,
                     'age':age})

len(info.batter_name.unique())   # 1661 (데이터프레임 길이는 1756으로 겹치는게 95개 존재)
info.loc[info.batter_name == '고우석',:]     # 동명이인 존재
(info['batter_name'].str[-1] == ')').sum()         # 마지막이 )로 끝나는 이름 -> (투)&(타)인 경우 40개 존재

info = info.loc[info['batter_name'].str[-1] != ')',:]     # (투)&(타)인 경우 삭제

info
pre_season
imsi = pd.concat([pre_season, info])

info.to_csv('info.csv')