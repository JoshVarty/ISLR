import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from pandas.plotting import boxplot

path = "../input/College.csv"
df = pd.read_csv(path)

#Set rownames equal to the first column (School name)
df = df.set_index(df.columns[0])

to_plot = df.iloc[:,0:10]
scatter_matrix(to_plot, alpha=0.2, figsize=(10,10), diagonal="kde")
plt.show()

outstate_private = df[["Outstate", "Private"]]
outstate_private.boxplot(by="Private")
plt.show()

df["Elite"] = "No"
df.loc[df["Top10perc"] > 50, "Elite"] = "Yes"
df["Elite"].describe()

outstate_elite = df[["Outstate", "Elite"]]
outstate_elite.boxplot(by="Elite")
plt.show()