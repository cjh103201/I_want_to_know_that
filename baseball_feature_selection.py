# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:10:30 2020

@author: KITCOOP
"""
run profile1
from sklearn.feature_selection import SelectFromModel

reg = pd.read_csv('C:/Users/KITCOOP/Documents/카카오톡 받은 파일/야구/Regular_Season_Batter.csv',
                  encoding='cp949')
reg.columns
len(reg.columns)

reg2 = reg.groupby(reg.batter_id).mean()
len(reg2.columns)
reg2 = reg2.iloc[:,1:]


reg2.iloc[:,19:]
reg3=reg2.iloc[:,0:19]


np.where(np.isnan(reg3))
reg3.iloc[305,305,305]






# 2. 불필요한 변수 제거
vseed = np.random.RandomState(0) #0으로 고정하는것 하고싶으면, 고정안해도됨
vcol = vseed.normal(size=(len(reg3), 10)) # noise변수 10개추가

# 3. 기존 데이터와 결합
np.hstack([reg3, vcol]).shape  # (345, 29)
reg_new = np.hstack([reg3, vcol])

# 4. 랜덤포레스트에 의한 모델 기반 변수 선택
m_rf = rf()  #튜닝후에 모델을 넣어야햠 (여기서는 생략)
m_fs2 = SelectFromModel(m_rf, threshold='median') # 추출비율 threshold='median':50%
m_fs2.fit(reg_new, reg2.OPS)




m_fs2.get_support() #True,False값 을 색인값으로 전달해서 설명변수 이름 추출가능하게됨
                    #뒤에는 추가한 noise변수이기때문에 전달하지않은상태
                    #  [m_fs2.get_support()]
# 5. 각 변수 중요도 출력
m_fs2.estimator_.feature_importances_ #변수중요도 추출할수있는 모델 -트리기반, 회귀기반




