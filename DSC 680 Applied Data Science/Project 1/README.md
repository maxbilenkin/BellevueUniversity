# Credit Card Customer Churn Prediction Using Machine Learning

## Project Overview

Customer retention is one of the most important challenges in the banking industry. Acquiring new credit card customers is expensive, while losing existing customers leads to direct revenue loss and reduced long-term profitability.

This project focuses on predicting credit card customer churn using machine learning models. By identifying customers who are likely to stop using their credit cards, banks can proactively implement retention strategies and reduce customer attrition.

---

## Business Problem

The banking industry is highly competitive, especially in the credit card market. Customers frequently receive competing offers from other financial institutions, making customer retention increasingly important.

The primary objective of this project is to identify behavioral and demographic factors associated with customer churn and develop machine learning models capable of predicting which customers are most likely to leave.

Early identification of high-risk customers allows banks to:

* Improve customer retention strategies
* Reduce marketing costs
* Increase long-term customer value
* Maintain stable recurring revenue

---

## Research Questions

* How accurately can machine learning models predict customer churn?
* What factors contribute the most to customer churn?
* Are there identifiable behavioral patterns among customers who leave?
* How can predictive analytics improve customer retention strategies?

---

## Dataset

This project uses the **BankChurners** dataset obtained from Kaggle.

Dataset Source:
https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers

### Dataset Characteristics

* 10,127 customer records
* 23 variables
* Customer demographics
* Credit card account information
* Transaction behavior metrics
* Churn classification target variable

### Key Features

* Age
* Gender
* Education Level
* Marital Status
* Income Category
* Credit Limit
* Total Transaction Amount
* Total Transaction Count
* Months Inactive
* Contact Frequency

### Target Variable

* `Attrition_Flag`

  * Existing Customer
  * Attrited Customer

---

## Tools & Technologies

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## Methods

### Data Preparation

* Removed unnecessary Naive Bayes columns to prevent data leakage
* Encoded categorical variables into numerical values
* Cleaned and validated the dataset
* Performed exploratory data analysis (EDA)

### Machine Learning Models

* Logistic Regression
* Random Forest

### Model Evaluation

* Accuracy Score
* ROC-AUC Score
* Confusion Matrix
* Feature Importance Analysis

---

## Exploratory Data Analysis

Several visualizations were created to identify patterns associated with customer churn, including:

* Churn Distribution Chart
* Age vs Churn Box Plot
* Credit Limit vs Churn Analysis
* Transaction Amount vs Churn
* Gender vs Churn
* Feature Importance Visualization

### Key Findings

* Transaction activity was one of the strongest indicators of churn
* Customers with lower transaction activity were significantly more likely to churn
* Credit limit showed limited predictive value
* Gender showed minimal influence on churn behavior
* Repayment and transaction behavior were more important than demographics

---

## Model Performance

### Logistic Regression

* Accuracy: 0.86

### Random Forest

* Accuracy: 0.9555
* ROC-AUC: 0.987

The Random Forest model significantly outperformed Logistic Regression and demonstrated strong predictive performance for identifying churned customers.

---

## Feature Importance

The most important predictors of churn included:

1. Total Transaction Amount
2. Total Transaction Count
3. Total Count Change Q4 to Q1
4. Total Revolving Balance

These findings suggest that declining customer activity is one of the strongest signals of future churn.

---

## Ethical Considerations

This project considered several ethical issues related to predictive analytics:

* Avoiding demographic discrimination
* Ensuring fair treatment across customer groups
* Responsible use of predictive modeling
* Using machine learning to support customer retention rather than penalize customers

---

## Challenges

* Class imbalance between existing and churned customers
* Feature selection and interpretability
* Preventing model overfitting
* Ensuring business usability of predictions

---

## Business Impact

Predictive churn models can help financial institutions:

* Detect at-risk customers earlier
* Improve customer retention
* Reduce customer acquisition costs
* Increase long-term profitability
* Support data-driven business decisions

---

## References

* Kaggle Dataset: BankChurners
  https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers

* Ngai, E. W. T., Xiu, L., & Chau, D. C. K. (2009). Application of data mining techniques in customer relationship management: A literature review.

* Verbeke, W., Dejaeger, K., Martens, D., Hur, J., & Baesens, B. (2012). New insights into churn prediction using data mining techniques.
