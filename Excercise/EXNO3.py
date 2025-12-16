import numpy as np


data = np.genfromtxt('task.csv',delimiter=',',skip_header=1)

print(f"length:{len(data)}\n"
      f"Dimension:{data.ndim}\n"
      f"Size:{data.size}\n"
      f"Shape:{data.shape}\n"
      f"Data Type:{data.dtype}"
)