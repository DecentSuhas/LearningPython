import pandas as pd
import numpy as np

info = np.array(['apple', 'berry', 'cherry', 'grapes', 'kiwi'])
panda_series = pd.Series(info)
#print(panda_series)

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)

x = ['python','pandas']
df = pd.DataFrame(x)
print(df)