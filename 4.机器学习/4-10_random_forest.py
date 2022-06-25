import numpy as np
from sklearn.ensemble import RandomForestClassifier

X = np.array([
    [9, 5, 6, "computer science"],
    [10, 1, 2, "computer science"],
    [1, 8, 1, "literature"],
    [4, 9, 3, "literature"],
    [0, 1, 10, "art"],
    [5, 7, 9, "art"]
])

Forest = RandomForestClassifier(n_estimators=10).fit(X[:, :-1], X[:,-1])

students = Forest.predict([
    [8, 6, 5],
    [3, 7, 9],
    [2, 2, 1]
])

print(students)