CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS reporting;

CREATE TABLE IF NOT EXISTS staging.customers (
    customer_id TEXT,
    gender TEXT,
    SeniorCitizen INT,
    Partner TEXT,
    Dependents TEXT,
    tenure INT,
    PhoneService TEXT,
    MultipleLines TEXT,
    InternetService TEXT,
    OnlineSecurity TEXT,
    OnlineBackup TEXT,
    DeviceProtection TEXT,
    TechSupport TEXT,
    StreamingTV TEXT,
    StreamingMovies TEXT,
    Contract TEXT,
    PaperlessBilling TEXT,
    PaymentMethod TEXT,
    MonthlyCharges FLOAT,
    TotalCharges TEXT,
    Churn TEXT,
    Email TEXT,
    Phone TEXT,
    Name TEXT
);
