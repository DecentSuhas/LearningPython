import matplotlib.pyplot as plt
import pandas as pd


# Make the dataframe for evaluation on Errorbars
df = pd.DataFrame({
    'insert': [0.0, 0.1, 0.3, 0.5, 1.0],
    'mean': [0.009905, 0.45019, 0.376818, 0.801856, 0.643859],
    'quality': ['good', 'good', 'poor', 'good', 'poor'],
    'std': [0.003662, 0.281895, 0.306806, 0.243288, 0.322378]})

print(df)

# Subplots as having two types of quality
fig, ax = plt.subplots()

for key, group in df.groupby('quality'):
   group.plot('insert', 'mean', yerr='std',
              label=key, ax=ax)
plt.show()