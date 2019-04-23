from sklearn.linear_model import LogisticRegression
lr = LogisticRegression().fit(train_data_finite, train_labels)
print(f"logistic regression score: {lr.score(test_data_finite, test_labels):f}")

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=500, random_state=0).fit(train_data_finite, train_labels)
print(f"random forest score: {rf.score(test_data_finite, test_labels):f}")

features_dummies_sub = pd.get_dummies(features[['pclass', 'sex', 'age', 'sibsp', 'fare']])
data_sub = features_dummies_sub.values

train_data_sub, test_data_sub, train_labels, test_labels = train_test_split(data_sub, labels, random_state=0)

imp = SimpleImputer()
imp.fit(train_data_sub)
train_data_finite_sub = imp.transform(train_data_sub)
test_data_finite_sub = imp.transform(test_data_sub)
                                         
lr = LogisticRegression().fit(train_data_finite_sub, train_labels)
print(f"logistic regression score w/o embark, parch: {lr.score(test_data_finite_sub, test_labels):f}")
rf = RandomForestClassifier(n_estimators=500, random_state=0).fit(train_data_finite_sub, train_labels)
print(f"random forest score w/o embark, parch: {rf.score(test_data_finite_sub, test_labels):f}")