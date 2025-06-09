import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
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

#Basic Checks
print(df.info())
print(df.describe())
print(df.isnull().sum())

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

df['Age'] = df['Phone'].apply(anonymize)
df['Gender'] = df['Name'].apply(anonymize)


# compute the KPIs 
churn_rate = df['Churn'].value_counts(normalize=True)['Yes'] * 100
print(f"Churn Rate: {churn_rate:.2f}%")

avg_revenue = df['MonthlyCharges'].mean()
print(f"Average Monthly Charges: ₹{avg_revenue:.2f}")

#KPI -1
df.groupby('ContractType')['Churn'].value_counts(normalize=True).unstack().plot(kind='bar', stacked=True)
plt.title('Churn by Contract Type')
plt.ylabel('Proportion')
plt.show()


#KPI- 2
fig = px.scatter(df, x='Tenure', y='MonthlyCharges', color='Churn',
                 title='Tenure vs Monthly Charges colored by Churn')
fig.show()


#write the updated dataframe to reporting schema in postgre
df.to_sql("customers", conn, schema='reporting', if_exists='replace', index=False)
