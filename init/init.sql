CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS reporting;

CREATE TABLE IF NOT EXISTS staging.customers(
    CustomerID TEXT,
    Age TEXT,
    Gender TEXT,
    Tenure TEXT,
    MonthlyCharges TEXT,
    ContractType TEXT,
    InternetService TEXT,
    TotalCharges TEXT,
    TechSupport TEXT,
    Churn TEXT
);
