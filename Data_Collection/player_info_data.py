import pandas as pd
import numpy as np

regular = pd.read_csv('regular_season_data.csv')
info = pd.read_csv('player_info.csv', encoding='CP949')

regular['team'] = regular['team'].replace({'해':'해태','K':'KIA','N':'NC','삼':'삼성','두':'두산','롯':'롯데','L':'LG','S':'SK',
                                           '현':'현대','쌍':'쌍방울','넥':'넥센','히':'히어로즈','키':'키움','O':'OB','빙':'빙그레',
                                           '한':'한화','k':'KT','M':'MBC','청':'청보','태':'태평양'})     # regular_season_data 팀 이름 info와 통일

pd.to_datetime(regular['birth'])     # 생년월일 0000-00-00이 존재 -> 15년도 조홍석 데이터
chs15_data = regular.loc[(regular['name'] == '조홍석') & (regular['year'] == 15), :]     # 15년도 조홍석 데이터
chs15_data['position'] = chs15_data['position'].replace(NA,'CF')                # 포지션이 NA로 되어있음 -> CF로 수정
chs15_data['birth'] = chs15_data['birth'].replace('0000-00-00','1990-02-23')    # 생년월일 1990-02-23으로 수정
regular.loc[(regular['name'] == '조홍석') & (regular['year'] == 15), :] = chs15_data   # 저장된 수정사항을 기존 regular dataframe에 덮어쓰기
regular['birth'] = pd.to_datetime(regular['birth'])    # 날짜형태로 변환
info['birthday'] = pd.to_datetime(info['birthday'])    # 날짜형태로 변환

regular = regular.loc[regular['position'].notnull(),:]    # 포지션이 null인 경우 제외
regular = regular.loc[regular['position'] != 'P',:]       # 포지션이 투수인 경우 제외

regular['position'].unique()     # 포지션이 현RF 형태인 경우 존재 -> 시즌 중간 팀이 바뀐경우 포지션에도 팀이 기록됨. 재가공 필요
position_imsi = regular.loc[regular['position'].map(lambda x : x not in ['C','1B','2B','3B','SS','LF','CF','RF','DH']),:]  # 팀 바뀐 경우 추출
position_imsi['position'].unique()          # 맨 앞 한자리가 팀으로 기록되어있으므로 앞자리 제외
position_imsi['position'] = position_imsi['position'].str[1:]   # 앞자리 제외하였음

position_imsi['position'].unique()          # ''인 경우 -> NA이므로 제외, P인경우도 제외
position_imsi = position_imsi.loc[position_imsi['position'] != '',:]
position_imsi = position_imsi.loc[position_imsi['position'] != 'P',:]

regular = regular.loc[regular['position'].map(lambda x : x in ['C','1B','2B','3B','SS','LF','CF','RF','DH']),:]  # 기존 정상적인 포지션을 가진 데이터
regular = pd.concat([regular,position_imsi], ignore_index=True) # 기존 정상적인 포지션을 가진 데이터에 가공된 position_imsi 결합

del regular['Unnamed: 0']  # 불필요 컬럼 제거
del info['Unnamed: 0']     # 불필요 컬럼 제거
del info['age']            # info의 나이 데이터는 시즌 별 나이와 맞지않아 제거

regular_merge = pd.merge(regular, info, left_on=['name','team','birth'], right_on=['batter_name','team','birthday'])
regular_merge.to_csv('regular_merge.csv')


