from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([
    [0, "No"],
    [10, "No"],
    [60, "Yes"],
    [90, "Yes"]
])
n = len(X)

model = LogisticRegression().fit(X[:, 0].reshape(n, 1), X[:, 1])

print(model.predict([[2], [12], [13], [40], [90]]))

for i in range (20):
    print("x=" + str(i) + " --> " + str(model.predict_proba([[i]])))