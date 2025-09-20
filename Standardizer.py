import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,StandardScaler, MinMaxScaler, RobustScaler, Normalizer
from sklearn import model_selection
from sklearn.model_selection import train_test_split,RepeatedKFold,cross_val_score
from plotnine import ggplot, aes, geom_tile, scale_fill_gradient, theme_minimal, theme, geom_boxplot
from plotnine import ggsave, scale_y_reverse, labs, scale_fill_gradient2,geom_line,geom_point,scale_color_manual,geom_text
import statsmodels.api as sm
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score,roc_curve, auc
from sklearn.neighbors import NearestNeighbors,KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier,RandomForestClassifier
import xgboost as xgb
from tqdm import tqdm


def standardize_data(features,response):
    
  
  #scale dataset
  feautre_scaler = StandardScaler()
  response_scaler = StandardScaler()
  feautre_scaler.fit(features)
  response_scaler.fit(response)
  
  features_scaled = feautre_scaler.transform(features) #scaled Features
  response_scaled = response_scaler.transform(response) # scaled Response

  
  
  features_scaled = pd.DataFrame(features_scaled, columns=features.columns)
  response_scaled = pd.DataFrame(response_scaled, columns=response.columns)
  return features_scaled,response_scaled,feautre_scaler,response_scaler