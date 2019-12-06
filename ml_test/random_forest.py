from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

from sklearn.metrics import accuracy_score

X, y = make_classification(n_samples=1000, n_features=4, n_informative=2, n_redundant=0, random_state=0, shuffle=False)
clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
clf.fit(X[:2], y[:2])
clf.fit(X[2:], y[2:])
result = clf.predict(X[:10])

print(accuracy_score(y[:10], result))

x = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
y = [1, 0, 0, 1]

clf2 = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
clf2.fit(x, y)
y_p = clf2.predict(x)
print(y_p)
print(accuracy_score(y, y_p))
print(clf2.predict([[0, 0]]))
