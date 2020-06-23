# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 16:55:41 2020

@author: HOON
"""

df = pd.read_csv('Temp_Data/total_daily_data.csv')
df = df[['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','name','team1','team2','개시시간','경기시간','관중',
    '구장','날짜','득점','안타','타수','타율','타점']]

dic = {'1땅':'우땅','2땅':'우땅','3땅':'좌땅','유땅':'좌땅','투땅':'중땅','1비':'우플','2비':'우플','3비':'좌플','유비':'좌플','투비':'중플','1안':'우안','2안':'우안',
       '3안':'좌안','유안':'좌안','투유병':'중병','투2병':'중병','2유병':'우병','유2병':'좌병','32병':'좌병','좌비':'좌플','우비':'우플','중비':'중플','좌희비':'좌플',
       '중희비':'중플','우희비':'우플','1파':'우플','2파':'우플','3파':'좌플','유파':'좌플','4구':'볼넷','좌중안':'좌안','우중안':'우안','좌중2':'좌2','좌중안':'좌안',
       '1번':'우땅','우중2':'우2','우파':'우플','1실':'우땅','우중홈':'우홈','1희번':'우땅','포비':'중플','포파':'중플','투희번':'중땅','투실':'중땅','유실':'좌땅',
       '투안':'중안','3직':'좌플','3희번':'좌땅','투직':'중플','좌중홈':'좌홈','3실':'좌땅','2직':'우플','포희번':'중땅','유직':'좌땅','2실':'우땅','좌중3':'좌3',
       '우중3':'우3','좌파':'좌플','좌병':'좌플','고4':'볼넷','유병':'좌병','스낫':'삼진','2병':'우병','포번':'중땅','투번':'중땅','3번':'좌땅','1유병':'우병','포안':'중안',
       '포땅':'중땅','1직':'우플','투희선':'중땅','좌실':'좌플','투희실':'중땅','야선':'','투포병':'중땅','투파':'중플','1병':'우병','타방':'볼넷','우희실':'우플','투3병':'중땅',
       '3병':'좌땅','포유병':'중땅','三二병':'좌땅','二땅':'우땅','一땅':'우땅','一비':'우플','三비':'좌플','三파':'좌플','二비':'우플','二실':'우땅','유二병':'좌땅',
       '一파':'우플','三안':'좌안','투二병':'중땅','一직':'우플','一희번':'우땅','二유병':'우땅','一번':'우땅','三실':'좌땅','二직':'우플','二안':'우안','一안':'우안', 
       '三번':'좌땅','二파':'우플','一실':'우땅','三병':'좌땅','三희번':'좌땅','一병':'우병','우실':'우플','二병':'우병','二희비':'우플','三직':'좌플','포병':'중병',
       '삼비':'삼진','포희실':'중땅','유포병':'좌병','32':'좌병','1포병':'우병','三땅':'좌땅','一유병':'우땅','포실':'중땅','포三병':'중병','一희비':'우플','一희선':'우땅',
       '삼선':'좌땅','포희선':'중땅','우직':'우플','3희선':'좌땅','유좌안':'좌안','투유안':'중안','투2안':'중안','투병':'중병','2우안':'우안','투3안':'좌안','2중안':'중안',
       '1우안':'우안','3유안':'좌안','유3안':'좌안','2번':'우땅','유중2':'중2','투중안':'중안','2중2':'중2','중실':'중플','투우안':'우안','3좌안':'좌안','투좌안':'좌안',
       '1희선':'우땅','3포병':'우병','유중안':'중안','3좌2':'좌2','투1안':'우안','12안':'우안','1우3':'우3','유좌2':'좌2','2포병':'우병','1우2':'우2','중희실':'중플',
       '3희실':'좌땅','좌직':'좌플','중직':'중플','3삼중':'좌병','2희비':'우플','1희실':'우땅','3유병':'좌병','투三병':'중병','三희실':'좌땅','三':'좌땅','二희실':'우땅',
       '유희번':'좌땅','투2':'중병','투중2':'중2','포3병':'중병','1희비':'우플','유2':'좌병','2희번':'우땅','투우2':'우2','2우2':'우2','22':'우2','2유안':'우안','2희실':'우땅',
       '三포병':'좌땅','一2':'우2','三2':'우2','一희실':'우땅','一三병':'우병','13병':'우땅','12':'우2','유번':'좌땅','투좌2':'좌2','유희비':'좌플','122':'우2','포2병':'중병',
       '유3병':'좌병','23병':'우병','一포병':'우병','二번':'우땅','병':'좌병','3중안':'좌안','2좌안':'중안','2좌2':'중2','유우안':'중안','3유2':'좌2','21병':'우땅','투포안':'중땅',
       '1중2':'우2','二희번':'우땅','三유병':'좌병','안':'우안','유우2':'좌2','좌희실':'좌플','三희선':'좌땅','三희비':'좌플','투1병':'중병','땅':'우땅'}

df.iloc[:,:9] = df.iloc[:,:9].applymap(lambda x : str(x).split('/')[0])     # 한 이닝 2타석 들어선 경우 -> 중2/ 유땅 이런식으로 나옴 -> 재가공 필요(앞에꺼만 추출)
df.iloc[:,:9] = df.iloc[:,:9].apply(lambda x : x.replace(dic))

left_go=[]; center_go=[]; right_go=[]; left_fly=[]; center_fly=[]; right_fly=[]; left_hit=[]; center_hit=[]; right_hit=[]; left_2=[]; center_2=[]; right_2=[]; left_3=[]; center_3=[];
right_3=[]; left_dp=[]; center_dp=[]; right_dp=[]; left_hr=[]; center_hr=[]; right_hr=[]; b4=[]; hbp=[]; so=[]; left_all=[]; center_all=[]; right_all=[]
# 좌땅,중땅,우땅, 좌플,중플,우플, 좌안,중안,우안, 좌2,중2,우2, 좌3,중3,우3, 좌병,중병,우병, 좌홈,중홈,우홈, 볼넷,사사구,삼진, 좌측타구, 중간타구, 우측타구

for i in range(len(df)):
    left_go.append((df.iloc[i,:9] == '좌땅').sum())
    center_go.append((df.iloc[i,:9] == '중땅').sum())
    right_go.append((df.iloc[i,:9] == '우땅').sum())
    
    left_fly.append((df.iloc[i,:9] == '좌플').sum())
    center_fly.append((df.iloc[i,:9] == '중플').sum())
    right_fly.append((df.iloc[i,:9] == '우플').sum())
    
    left_hit.append((df.iloc[i,:9] == '좌안').sum())
    center_hit.append((df.iloc[i,:9] == '중안').sum())
    right_hit.append((df.iloc[i,:9] == '우안').sum())
    
    left_2.append((df.iloc[i,:9] == '좌2').sum())
    center_2.append((df.iloc[i,:9] == '중2').sum())
    right_2.append((df.iloc[i,:9] == '우2').sum())
    
    left_3.append((df.iloc[i,:9] == '좌3').sum())
    center_3.append((df.iloc[i,:9] == '중3').sum())
    right_3.append((df.iloc[i,:9] == '우3').sum())
    
    left_dp.append((df.iloc[i,:9] == '좌병').sum())
    center_dp.append((df.iloc[i,:9] == '중병').sum())
    right_dp.append((df.iloc[i,:9] == '우병').sum())
    
    left_hr.append((df.iloc[i,:9] == '좌홈').sum())
    center_hr.append((df.iloc[i,:9] == '중홈').sum())
    right_hr.append((df.iloc[i,:9] == '우홈').sum())
    
    b4.append((df.iloc[i,:9] == '볼넷').sum())
    hbp.append((df.iloc[i,:9] == '사구').sum())
    so.append((df.iloc[i,:9] == '삼진').sum())
    
    left_all.append((df.iloc[i,:9].str[0] == '좌').sum())
    center_all.append((df.iloc[i,:9].str[0] == '중').sum())
    right_all.append((df.iloc[i,:9].str[0] == '우').sum())
    
df['좌땅']=left_go
df['중땅']=center_go
df['우땅']=right_go
df['좌플']=left_fly
df['중플']=center_fly
df['우플']=right_fly
df['좌안']=left_hit
df['중안']=center_hit
df['우안']=right_hit
df['좌2']=left_2
df['중2']=center_2
df['우2']=right_2
df['좌3']=left_3
df['중3']=center_3
df['우3']=right_3
df['좌병']=left_dp
df['중병']=center_dp
df['우병']=right_dp
df['좌홈']=left_hr
df['중홈']=center_hr
df['우홈']=right_hr
df['볼넷']=b4
df['사구']=hbp
df['삼진']=so
df['좌측타구']=left_all
df['중간타구']=center_all
df['우측타구']=right_all


df.to_csv('Temp_data.csv')
