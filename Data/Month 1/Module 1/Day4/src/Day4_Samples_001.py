
---

### Code Sample for Day 4
Below is a single Python file (`Day4_Samples_001.py`) with five sample programs tailored to Module 4: Data Analytics Basics (Days 16-20), focusing on Day 4's topics of introducing data analytics tools, data cleaning, and wrangling. Note that a sample CSV file (`sample_data.csv`) is assumed; you can create a simple one with columns like `name`, `age`, and `score` for testing.

```python
# Day4_Samples_001.py
# Program 1: Loading a CSV File with pandas
import pandas as pd
data = pd.read_csv("sample_data.csv")
print("First 5 rows:")
print(data.head())

# Program 2: Checking Data Types
print("Data types:")
print(data.dtypes)

# Program 3: Handling Missing Data
data.fillna(0, inplace=True)
print("Missing values count after filling:")
print(data.isnull().sum())

# Program 4: Removing Duplicates
data_no_duplicates = data.drop_duplicates()
print("Rows after removing duplicates:", len(data_no_duplicates))

# Program 5: Data Transformation with New Column
data['age_plus_score'] = data['age'] + data['score']
print("Data with new column 'age_plus_score':")
print(data.head())