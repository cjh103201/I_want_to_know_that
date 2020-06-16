import pandas as pd

df_weather = pd.read_csv('dailyGame_weather_merge.csv')
df_ground = pd.read_csv('ground_info.csv')

df_ground = df_ground.iloc[:,:4]    # 불필요 컬럼 제거
weather_ground_merge = pd.merge(df_weather, df_ground, left_on='ground', right_on='name')

del weather_ground_merge['지점']
del weather_ground_merge['지점명']
del weather_ground_merge['일시']
del weather_ground_merge['name']

weather_ground_merge.to_csv('weather_ground_merge.csv')
