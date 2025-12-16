import pandas as pd
import numpy as np

data = pd.read_csv('task.csv')


print(f"The given the File contact:\n{data}")
print(f"The Minimum values:\n{data.min()}")
print(f"The maximum values:\n{data.max()}")
print(f"The mean of the mark1:\n{data['mark1'].mean()}")
print(f"The mean of the mark2:\n{data['mark2'].mean()}")
print(f"The median of the mark 1:\n{data['mark1'].median()}")
print(f"The median of the mark 2:\n{data['mark2'].median()}")
print(f"The correction and Co efficient Value:\n{np.corrcoef(data['mark1'],data['mark2'])}")
print(f"The standard deviation Value:{np.std(data['mark1'])}")
print(f"The standard deviation Value:{np.std(data['mark2'])}")
print(f"The CumSum Values:\n{data.cumsum()}")

