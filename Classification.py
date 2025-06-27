import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, Lasso, Ridge
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier
import pickle
import streamlit as st
import joblib

# Load the dataset 

path = 'C:/Users/Trois/Downloads/Video/Data Science/Month 4/Datasets/Expresso_churn_dataset.csv'

data = pd.read_csv(path)

print(data.head())

data.info()

data.describe()


# Data Prifiling

#report = ProfileReport(data, title= 'Expresso_churn Profiling report')

#report.to_notebook_iframe()

# Heatmap

plt.figure(figsize=(12,8))
data_heatmap = data.select_dtypes(exclude='object')
sns.heatmap(data_heatmap.corr(), annot=True)
plt.show()

# Output data distribution

dct_chrun = {'CHURN': {1:'Chrun', 0: 'Not Churn'}}
label = data.CHURN.value_counts().reset_index().replace(dct_chrun)

plt.pie(data.CHURN.value_counts(), labels=label['CHURN'], autopct='%1.1f%%')
plt.title('Output data ditribution')
plt.show()

# Checking for missing values

data.isna().sum()

# Frequence des valeurs manquantes

#data.isna().mean().sort_values(ascending=False) * 100

# Dropping the irrlevant columns

data.drop(columns=['user_id','ZONE1', 'ZONE2', 'MRG'], inplace= True) # Drop ZONE1 and ZONE2 columns, since the null values on these features exceeds 90 % of the dataset


# Check the ditribution of the data on the
num_col = data.select_dtypes(exclude='object').columns

plt.figure(figsize=(20,15))
for i, col in enumerate(num_col, 1):
    plt.subplot(4, 4, i)
    plt.hist(data[col], bins= 50)
    plt.title(col)
plt.tight_layout()
plt.show()

# Handling the missing values

col_nul = list()
cat_col = data.select_dtypes(include='object').columns
num_col = data.select_dtypes(exclude='object').columns

for col in cat_col:
    if data[col].isna().sum():
        data[col] = data[col].fillna(data[col].mode()[0])

for col in num_col:
    if data[col].isna().sum():
        data[col] = data[col].fillna(data[col].median())
        

# checking for duplicat

data.duplicated().sum()

# Dropping duplicate values

data.drop_duplicates()

# Encoding the data

data_2 = data.copy()

encoder = LabelEncoder()

object_col = data.select_dtypes(include='object').columns

for col in object_col:
    data[col] = encoder.fit_transform(data[col])


# Select the input and output data for ML

x= data.drop(columns='CHURN')

y= data.CHURN

# Splitting the data

x_train, x_test, y_train, y_test = train_test_split(x, y , test_size=0.2, random_state= 33)


# training the model

model = LogisticRegression(max_iter=100)

model.fit(x_train, y_train)

# Make predictipn

predict = model.predict(x_test)

# Evaluate the model

classification_report(y_test, predict)

print('Accuracy', accuracy_score(predict, y_test))

# Mapping the encoded columns with the original values

dct_region = dict(zip(data_2.REGION.unique(), data.REGION.unique()))

dct_tenure = dict(zip(data_2.TENURE.unique(), data.TENURE.unique()))

dct_top_pack = dict(zip(data_2.TOP_PACK.unique(), data.TOP_PACK.unique()))

# save the mapping dictionnary 

dct_map_cat_data = {'dct_region': dct_region, 'dct_tenure':dct_tenure, 'dct_top_pack':dct_top_pack}


# Save the model to a file

joblib.dump(model, 'model.pkl')
joblib.dump(dct_map_cat_data, 'dct_map_cat_data.pkl')



#with open (data.plk)
