# DSC 630 – Predictive Analytics

## Course Overview
This course integrates topics covered in previous data science courses into a comprehensive applied project. Students are responsible for defining a problem, acquiring and preparing data, performing analysis, and presenting results. Advanced analytical techniques using Python and R are applied to explore real-world datasets and generate actionable insights.

## Project: Identifying Key Characteristics of Potential Customers Likely to Sign Up for a New Credit Card

### Project Description
Acquiring new credit card customers is a major challenge in today’s competitive financial environment. Many consumers already possess one or more credit cards and often keep them long-term, making it difficult for banks to attract new users. However, certain segments of the population, such as individuals without credit cards or those who frequently switch financial products, may be more open to adopting a new card.

This project focuses on identifying the characteristics of individuals who are more likely to sign up for a new credit card. By analyzing customer demographic and behavioral data, predictive models can help banks identify high-potential customers and improve marketing strategies.

### Business Justification
Understanding which individuals are more likely to respond to financial product offers allows banks to significantly improve their marketing campaigns. Instead of relying on broad marketing strategies, banks can focus on targeted outreach toward customers with a higher probability of adoption.

This approach can help financial institutions:

- Reduce marketing costs  
- Increase conversion rates  
- Improve return on investment (ROI)  
- Transition from mass marketing to more personalized customer acquisition strategies  

### Dataset
This project uses the **Bank Marketing Dataset** from the UCI Machine Learning Repository.

The dataset contains information about marketing campaigns conducted by a Portuguese banking institution and includes whether a client subscribed to a financial product. Although the original target variable relates to term deposit subscriptions, the response behavior can be adapted to model customer decisions related to credit card adoption.

Key features in the dataset include:

- **Demographics:** age, job, marital status, education  
- **Financial attributes:** default history, housing loan, personal loan  
- **Campaign details:** contact method, number of contacts, previous campaign outcomes  
- **Target variable:** whether the client subscribed to the product (yes/no)

This dataset is well suited for classification modeling and helps identify individuals likely to respond positively to financial product offers.

### Tools & Technologies
- **Python**
- **Pandas**
- **Scikit-learn**
- **Matplotlib**
- **Jupyter Notebook**

### Methodology
The project followed a structured predictive analytics workflow:

1. Data cleaning and preprocessing  
2. Exploratory Data Analysis (EDA)  
3. Feature selection and engineering  
4. Train/test data split  
5. Application of supervised classification models including:
   - Logistic Regression
   - Decision Trees
   - Random Forest
6. Model evaluation using metrics such as accuracy, precision, recall, and ROC-AUC  
7. Interpretation of feature importance and development of business recommendations

### Key Outcome
The analysis demonstrates how predictive modeling can help financial institutions identify potential customers who are more likely to adopt new credit cards. By targeting these high-probability customers, banks can improve marketing efficiency and increase overall profitability.
