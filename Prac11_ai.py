import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

df = pd.read_csv("/content/Student_Performance_2026.csv")

print("Columns:", df.columns)

X = df[['online_study_hours']]
Y = df['current_sem_CGPA']

df['modified_hours'] = df['online_study_hours'] + np.random.normal(0, 0.5, len(df))
X_modified = df[['modified_hours']]

model = LinearRegression()
model.fit(X, Y)
Y_pred = model.predict(X)

model_mod = LinearRegression()
model_mod.fit(X_modified, Y)
Y_pred_mod = model_mod.predict(X_modified)

plt.scatter(X, Y, label="Original Data")
plt.plot(X, Y_pred, label="Regression Line", linestyle='dashed')
plt.scatter(X_modified, Y, label="Modified Data")
plt.plot(X_modified, Y_pred_mod, label="Modified Regression", linestyle='dotted')
plt.xlabel("Study Hours")
plt.ylabel("CGPA")
plt.title("Linear Regression Analysis")
plt.legend()
plt.show()

mse = mean_squared_error(Y, Y_pred)
mae = mean_absolute_error(Y, Y_pred)

print("\nError Metrics:")
print("MSE:", mse)
print("MAE:", mae)

new_hours = np.array([[5]])
prediction = model.predict(new_hours)

print("\nPrediction for 5 study hours:", prediction[0])