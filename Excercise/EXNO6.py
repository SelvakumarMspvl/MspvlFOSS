
import pandas as pd

d1 = pd.read_csv('exno6.csv')
d2 = pd.read_csv('exno6(1).csv')

combined_df = pd.concat([d1, d2])
combined_df = combined_df.drop_duplicates()
combined_df = combined_df.reset_index(drop=True)
print("Combined DataFrame after removing duplicates:\n",combined_df)