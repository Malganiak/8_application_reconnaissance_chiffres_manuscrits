# Librairies
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Read datasets
df_test = pd.read_csv('mnist_test.csv')
df_train = pd.read_csv('mnist_train.csv')

# Test/train split 
X_train = df_train.drop('label', axis = 1)
y_train = df_train.label
X_test = df_test.drop('label', axis = 1)
y_test = df_test.label

# Fit the model on training set
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train.values, y_train.values)

# Save model
filename = 'knn_digits'
joblib.dump(model, filename)