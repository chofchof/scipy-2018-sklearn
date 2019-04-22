from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.25,
                                                    random_state=1234,
                                                    stratify=y)

X_trainsub, X_valid, y_trainsub, y_valid = train_test_split(X_train, y_train,
                                                            test_size=0.5,
                                                            random_state=1234,
                                                            stratify=y_train)

for k in range(1, 20):
    knn = KNeighborsClassifier(n_neighbors=k)
    train_score = knn.fit(X_trainsub, y_trainsub).score(X_trainsub, y_trainsub)
    valid_score = knn.score(X_valid, y_valid)
    print(f"k: {k}, Train/Valid Acc: {train_score:.3f}/{valid_score:.3f}")


knn = KNeighborsClassifier(n_neighbors=9)
knn.fit(X_train, y_train)
print(f"k=9 Test Acc: {knn.score(X_test, y_test):.3f}")