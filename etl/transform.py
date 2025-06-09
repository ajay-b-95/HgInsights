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
    'TotalCharges': '0',
    'Email': 'unknown@example.com',
    'Phone': '0000000000',
    'Name': 'Anonymous'
}, inplace=True)

# Anonymize PII
df['Email'] = df['Email'].apply(anonymize)
df['Phone'] = df['Phone'].apply(anonymize)
df['Name'] = df['Name'].apply(anonymize)

df.to_sql("customers", conn, schema='reporting', if_exists='replace', index=False)
