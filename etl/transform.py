import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import plotly.express as px
from sqlalchemy import create_engine
import hashlib
import os


def anonymize(value):
    return hashlib.sha256(str(value).encode()).hexdigest()

# conn = psycopg2.connect(
#     host='postgres',
#     database='postgres',
#     user='postgres',
#     password='postgres'
# )


engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres:5432/postgres')


df = pd.read_csv('/data/telecom_churn.csv')
print('df to show')
print(df)


#replace "None" with Null in df
df.replace("None", pd.NA, inplace=True)

#Basic Checks
print(df.info())
print(df.describe())
print(df.isnull().sum())

#writing raw to staging area
df.to_sql("customers", engine, schema='staging', if_exists='replace', index=False)


# Handle missing values (we can impute the standard values if givn by business
df.fillna({
    'CustomerID': 'unknown_id',
    'Age': '0',
    'Gender': 'Unknown',
    'Tenure': '0',
    'MonthlyCharges': '0',
    'ContractType': 'Unknown',
    'InternetService': 'Unknown',
    'TotalCharges': '0',
    'TechSupport': 'Unknown',
    'Churn': 'Unknown'
}, inplace=True)

#handling attributes with numbers 
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Tenure'].fillna(df['Tenure'].median(), inplace=True)
df['MonthlyCharges'].fillna(df['MonthlyCharges'].median(), inplace=True)
df['TotalCharges'].fillna('0', inplace=True) 


print(df)

avg_revenue = df['MonthlyCharges'].mean()
print(f"Average Monthly Charges: ₹{avg_revenue:.2f}")



#write the updated dataframe to reporting schema in postgre
# df.to_sql("customers", conn, schema='reporting', if_exists='replace', index=False)
# Use engine (not raw conn)
df.to_sql("customers", engine, schema='reporting', if_exists='replace', index=False)
