# Data Prepocessing Template from Machine Learning A-Z - SuperDataScience
# Input by Ryan L Buchanan 31AUG20

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1 ].values

print(X)
print(y)

# Taking care of the missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(X)

# Encoding categorical data


# Encoding the Independent Variable


# Encoding the Dependent Variable




