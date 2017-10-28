import pandas as pd

path = "../input/College.csv"
df = pd.read_csv(path)

#Set rownames equal to the first column (School name)
df = df.set_index(df.columns[0])