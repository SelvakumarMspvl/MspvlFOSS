import pandas as pd

data = pd.read_csv('ex05.csv')
print(f"Original Data:\n{data}")
MissingData = data.isnull().sum()
print(f"Missing data:\n{MissingData}")
data['mark1'] = data['mark1'].fillna(65)
data['mark2'] = data['mark2'].fillna(data['mark2'].mean())
print(f"Data after filling missing data:\n{data}")
