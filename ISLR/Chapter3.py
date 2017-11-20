import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from pandas.plotting import boxplot

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

boston = load_boston()
data = np.transpose(boston.data)
print("Shape:", data.shape)
print("Feature Names:", boston.feature_names)


lstat = boston.feature_names[12]
lstat_data = data[12]

test = LinearRegression()
Y = boston.target.reshape(506,1)
X = lstat_data.reshape(506,1)
result = test.fit(X=X, y=Y)
