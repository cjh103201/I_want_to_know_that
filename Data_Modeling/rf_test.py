
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

    
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



# LSTM
from keras.layers.core import Dense,Activation,Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential

def normalised_windows(window_data):
    normalised_data = []
    for window in window_data:
        normalised_window = [((float(p) / float(window[0])) - 1) for p in window]
        normalised_data.append(normalised_window)
    return normalised_data



##
regular['year'] == 2010





