import pandas as pd
import psycopg2
import hashlib
import os

def anonymize(value):
    return hashlib.sha256(str(value).encode()).hexdigest()

conn = psycopg2.connect(
    host='postgres',
    database='postgres',
    user='postgres',
    password='postgres'
)

df = pd.read_sql("SELECT * FROM staging.customers", conn)

# Handle missing values
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

df['Age'] = df['Phone'].apply(anonymize)
df['Gender'] = df['Name'].apply(anonymize)

df.to_sql("customers", conn, schema='reporting', if_exists='replace', index=False)
