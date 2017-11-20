import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from pandas.plotting import boxplot

#Question 8: College
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


p_undergrads, p_bins = np.histogram(df["P.Undergrad"])
f_undergrads, f_bins = np.histogram(df["F.Undergrad"], bins=p_bins)

width = (p_bins[1] - p_bins[0]) / 3

fix,ax = plt.subplots()
a = ax.bar(p_bins[:-1], p_undergrads, width=width, facecolor='cornflowerblue', label="Part time")
b = ax.bar(f_bins[:-1]+width, f_undergrads, width=width, facecolor='seagreen', label="Full time")

plt.legend(handles=[a, b])
plt.show()


#Question 9: Auto
auto_path = "../input/Auto.csv"
df = pd.read_csv(auto_path)

#Set rownames equal to the last column "name"
df = df.set_index(df.columns[-1])

#Replace unknown quantities with NaN and convert to float
df[["horsepower"]] = df[["horsepower"]].replace("?", np.nan)
df[["horsepower"]] = df[["horsepower"]].astype(np.float)

desc = df.describe()
means1 = desc.loc["mean"]
mins1 = desc.loc["min"]
maxs1 = desc.loc["max"]
stds1 = desc.loc["std"]

#Drop 10 to 85
df2 = df.drop(df.index[10:85])
desc2 = df2.describe()
means2 = desc2.loc["mean"]
mins2 = desc2.loc["min"]
maxs2 = desc2.loc["max"]
stds2 = desc2.loc["std"]

print(means1)
print(means2)

print(mins1)
print(mins2)

print(maxs1)
print(maxs2)

print(stds1)
print(stds2)


