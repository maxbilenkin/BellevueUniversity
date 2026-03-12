# DSC 540 – Data Preparation

## Course Overview
This course prepares students to handle **complex, variable, and unstructured data**. Techniques for acquiring, cleaning, transforming, and preparing datasets for analysis are emphasized. Tools include **Python, SQL**, and APIs to automate data preparation tasks.

## Course Project
The project explored **alcohol consumption and its effects on health**, specifically cardiovascular disease. The objective was to examine potential correlations between alcohol intake and heart-related health outcomes.

### Data Sources
1. **Heart Failure Clinical Records (Flat File)**
   - 299 patient records with 13 health-related variables (blood pressure, diabetes, smoking, age, etc.)
   - Source: [Kaggle](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data)
   - File: `heart_failure_clinical_records_dataset.csv`
   
2. **WHO Global Health Observatory (API)**
   - 12,936 rows, 25 columns of country-level alcohol consumption and related health statistics
   - Source: [WHO GHO OData API](https://www.who.int/data/gho/info/gho-odata-api)

3. **Wikipedia Alcohol Consumption per Capita (Web Scraping)**
   - 196 rows for total consumption, 189 rows for type-specific (beer, wine, spirits)
   - Source: [Wikipedia](https://en.wikipedia.org/wiki/List_of_countries_by_alcohol_consumption_per_capita)

### Analytical Approach
- **Data Cleaning & Standardization:** Handle missing values, standardize country names, ensure numerical consistency
- **Correlation Analysis:** Compare alcohol consumption trends with heart disease risk factors across datasets
- **Indirect Integration:** Since patient-level and country-level datasets cannot be directly merged, trends were compared across sources to identify meaningful patterns
- **Statistical Methods:** Applied exploratory data analysis and correlation tests to assess relationships

### Challenges
- **Data Merging:** No common keys across all datasets; indirect comparison required
- **Format Variability:** Combining medical records, API data, and web-scraped data required careful standardization
- **Correlation vs. Causation:** Observed trends indicate associations but not direct causality

### Ethical Considerations
- **Privacy & Sensitivity:** Patient data is anonymized but handled responsibly
- **Responsible Interpretation:** Avoid over-interpreting correlations as causation
- **Public Health Relevance:** Analysis can inform awareness and policy regarding alcohol consumption and cardiovascular health

### Project Outcomes
- Identified patterns connecting alcohol consumption with cardiovascular risk factors
- Highlighted the need to consider multiple health variables when interpreting alcohol-related data
- Demonstrated data preparation skills for integrating diverse datasets and preparing them for meaningful analysis

## Repository Contents
This folder contains all datasets, cleaned data, scripts, and reports associated with DSC 540.
