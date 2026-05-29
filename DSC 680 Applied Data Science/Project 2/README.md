# Predicting Credit Card Customer Default Risk Using Machine Learning

## Project Overview

Credit card default risk is a major concern for financial institutions because unpaid balances can lead to significant financial losses. Identifying customers who are likely to default before it happens allows banks to reduce risk, improve lending decisions, and proactively support customers experiencing financial difficulties.

This project applies machine learning techniques to predict whether a credit card customer is likely to default on their next monthly payment. Using demographic, financial, and repayment history data, multiple classification models were trained and evaluated to identify key factors associated with default risk.

---

## Business Problem

Banks issue thousands of credit cards to consumers, but not all customers repay their balances on time. Missed payments and defaults can negatively impact profitability and increase financial risk.

Traditional rule-based systems may fail to detect complex patterns in customer behavior. Machine learning provides a more advanced approach by analyzing large datasets to identify patterns associated with default risk.

The primary objective of this project was to build predictive models capable of identifying high-risk customers before default occurs.

---

## Dataset

This project used the **Default of Credit Card Clients Dataset** from the UCI Machine Learning Repository.

Dataset Source:

https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset

### Dataset Characteristics

* 30,000 customer records
* 25 variables
* Taiwan credit card client data
* Combination of:

  * demographic information
  * billing history
  * repayment behavior
  * payment amounts

### Target Variable

* `default.payment.next.month`

  * 1 = default
  * 0 = non-default

---

## Technologies & Tools Used

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## Machine Learning Models

The following classification models were implemented:

### Logistic Regression

Used as a baseline classification model to predict default probability.

### Random Forest Classifier

Used to improve prediction performance and better capture nonlinear relationships within the data.

---

## Project Workflow

1. Data loading and preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature engineering and scaling
4. Train-test split
5. Model training
6. Model evaluation
7. Visualization and interpretation of results

---

## Data Visualization & Analysis

Several visualizations were created to better understand customer behavior and default patterns:

* Correlation Heatmap
* Default Distribution Chart
* Gender vs Default Analysis
* Age Distribution Analysis
* Repayment Status Analysis
* Feature Importance Chart
* Confusion Matrices
* ROC Curve

---

## Key Findings

### Repayment History Was the Strongest Predictor

Customers with delayed payments had significantly higher default risk.

### Younger Customers Showed Higher Default Frequency

Default rates were generally higher among younger age groups.

### Random Forest Performed Better

Random Forest slightly outperformed Logistic Regression and handled class imbalance more effectively.

### Dataset Imbalance Affected Performance

Approximately 22% of customers defaulted, making prediction more challenging.

---

## Model Evaluation

### Logistic Regression

* Accuracy: Approximately 81%
* Strong at predicting non-default customers
* Lower recall for identifying actual defaults

### Random Forest

* Accuracy: Approximately 81.6%
* Better overall default detection
* Improved handling of imbalanced classes

Evaluation metrics included:

* Accuracy
* Precision
* Recall
* ROC-AUC Score
* Confusion Matrix

---

## Business Impact

This project demonstrates how machine learning can support:

* Credit risk assessment
* Fraud and loss prevention
* Proactive customer monitoring
* Improved lending decisions
* Financial risk management

Banks can use predictive analytics to identify high-risk customers earlier and implement preventive actions before defaults occur.

---

## Ethical Considerations

While machine learning can improve financial decision-making, predictive models should be used responsibly.

Important considerations include:

* avoiding demographic discrimination
* maintaining customer privacy
* using human oversight in lending decisions
* ensuring model transparency and fairness

---

## Future Improvements

Potential future enhancements include:

* Hyperparameter tuning
* Additional ensemble models
* SMOTE or advanced imbalance handling techniques
* Real-time prediction systems
* Explainable AI (XAI) methods

---

## Presentation

The project presentation included:

* business problem overview
* dataset explanation
* exploratory analysis
* machine learning results
* model comparisons
* business recommendations
* ethical considerations

---

## Author

Maxim Bilenkin

Bellevue University
Master of Science in Data Science
