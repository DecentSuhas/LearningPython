import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'Age' : [14,45,86,2,32,56,94,58]
})

plt.hist(df["Age"])
plt.show()