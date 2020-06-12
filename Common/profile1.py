import pandas as pd
import numpy as np

from math import trunc

from numpy import nan as NA
from pandas import Series
from pandas import DataFrame

import matplotlib.pyplot as plt

# 데이터 셋
from sklearn.datasets import load_iris as iris
from sklearn.datasets import load_breast_cancer as cancer

# 분석
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.neighbors import KNeighborsRegressor as knn_r

from sklearn.tree import DecisionTreeClassifier as dt
from sklearn.tree import DecisionTreeRegressor as dt_r

from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.ensemble import RandomForestRegressor as rf_r

from sklearn.ensemble import GradientBoostingClassifier as gb
from sklearn.ensemble import GradientBoostingRegressor as gb_r

# from xgboost.sklearn import XGBClassifier as xgb
# from xgboost.sklearn import XGBRegressor as xgb_r

from sklearn.svm import SVC

from sklearn.decomposition import PCA

from sklearn.preprocessing import PolynomialFeatures

# scale
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

# feauter selection
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import RFE

# CV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

from sklearn.model_selection import GridSearchCV

# LR
from sklearn.svm import LinearSVC
from sklearn.linear_model import LinearRegression

###################
import mglearn

import os
# from sklearn.tree import export_graphviz
# import graphviz

from mpl_toolkits.mplot3d import Axes3D, axes3d

import imageio

import statsmodels.api as sm

####################

# 딥러닝
import tensorflow as tf
import keras

import numpy as np

from keras.models import Sequential
from keras.layers import Dense

from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder

###################
# 모델 시각화
from keras.utils import plot_model
