birth = [i.split(' ')[1] for i in birth]    # 생년월일 1995-12-14 에서 뒤에꺼만 추출
birth = pd.to_datetime(birth)
height_weight = [i.split(' ')[1] for i in height_weight]    # 000cm/00kg 만 추출
height = [i.split('/')[0] for i in height_weight]    # 키 추출
weight = [i.split('/')[1] for i in height_weight]    # 몸무게 추출
team = [i.split(' ')[1] for i in team]      # 팀 추출

(datetime.today() - info['birthday'])/365     # (현재 - 생년월일) / 365 -> 나이 생성하기위해
age = [i.days for i in (datetime.today() - info['birthday'])/365]    # 나이 생성

info = pd.DataFrame({'name':name,
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

regular_season_data = pd.read_csv('Data/regular_season_data.csv', encoding='UTF-8')

regular_season_merge = pd.merge(regular_season_data, info, on='name')

regular_season_data = regular_season_data.set_index('Unnamed: 0')
regular_season_merge.team_x.unique()     # regular_season_data에 기록된 팀 이름 재가공 필요
regular_season_merge.team_x = regular_season_merge.team_x.replace({'해':'해태','K':'KIA','N':'NC','삼':'삼성','두':'두산','롯':'롯데','L':'LG','S':'SK','현':'현대',
                                                                   '쌍':'쌍방울','넥':'넥센','히':'히어로즈','키':'키움','O':'OB','빙':'빙그레','한':'한화','k':'KT',
                                                                   'M':'MBC','청':'청보','태':'태평양'})

del regular_season_merge['team_y']      # player_info에서 가져온 팀 이름 정보 제거
regular_season_merge = regular_season_merge.rename({'team_x':'team'}, axis=1)   # team_x 컬럼 이름 team으로 변경

regular_season_merge = regular_season_merge.loc[regular_season_merge.position != 'P',:]     # 투수 기록 제거

# 시즌정보 1995 형태로 재가공 필요
new_year = []
for i in regular_season_merge['year']:
    if i < 10:
        i = '200' + str(i)
    elif i >= 82:
        i = '19' + str(i)
    else:
        i = '20' + str(i)
    new_year.append(i)

regular_season_merge['year'] = new_year

# 기존 선수들 정보(player_info)의 나이는 시즌 별 나이와 맞지 않음 -> 재가공 필요
del regular_season_merge['age']     # 기존 나이 컬럼 제거

season_date = pd.to_datetime(regular_season_merge['year'] + '-01-01')    # 시즌년도를 1995-12-14 형태로 재가공
regular_season_merge['age'] = [i.days for i in ((season_date - regular_season_merge['birthday']) / 365)]     # (시즌 년도 - 생년월일) / 365 -> 시즌 당시 나이

regular_season_merge.to_csv('regular_season_merge.csv')






