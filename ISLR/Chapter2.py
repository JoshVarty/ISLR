import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

path = "../input/College.csv"
df = pd.read_csv(path)

#Set rownames equal to the first column (School name)
df = df.set_index(df.columns[0])

to_plot = df.iloc[:,0:10]
scatter_matrix(to_plot, alpha=0.2, figsize=(10,10), diagonal="kpe")
plt.show()