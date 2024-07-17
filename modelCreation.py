from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from catboost import CatBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

import pandas as pd
import pickle as pkl

data = pd.read_csv('dataset/phishing.csv')
data = data.drop(['Index', 'WebsiteTraffic'], axis=1)

X = data.drop(['class'], axis=1)
y = data['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


model_Log = LogisticRegression()
model_Log.fit(X_train, y_train)
print(f"Logistic Regression (testing) : {model_Log.score(X_test, y_test)}")
print(f"Logistic Regression (training) : {model_Log.score(X_train, y_train)}")

model_gbc = GradientBoostingClassifier()
model_gbc.fit(X_train, y_train)
print(f"GradientBoostingClassifier (testing) : {model_gbc.score(X_test, y_test)}")
print(f"GradientBoostingClassifier (training) : {model_gbc.score(X_train, y_train)}")

model_rfc = RandomForestClassifier()
model_rfc.fit(X_train, y_train)
print(f"RandomForestClassifier (testing) : {model_rfc.score(X_test, y_test)}")
print(f"RandomForestClassifier (training) : {model_rfc.score(X_train, y_train)}")

model_dtc = DecisionTreeClassifier()
model_dtc.fit(X_train, y_train)
print(f"DecisionTreeClassifier (testing) : {model_dtc.score(X_test, y_test)}")
print(f"DecisionTreeClassifiern (training) : {model_dtc.score(X_train, y_train)}")

# model_Log = LogisticRegression()
# model_Log.fit(X_train, y_train)
# print(f"Logistic Regression (testing) : {model_Log.score(X_test, y_test)}")
# print(f"Logistic Regression (training) : {model_Log.score(X_train, y_train)}")

model_svc = SVC()
model_svc.fit(X_train, y_train)
print(f"SVC (testing) : {model_svc.score(X_test, y_test)}")
print(f"SVC(training) : {model_svc.score(X_train, y_train)}")

# model_cbc = CatBoostClassifier()
# model_cbc.fit(X_train, y_train)
# print(f"CatBoostClassifier (testing) : {model_cbc.score(X_test, y_test)}")
# print(f"CatBoostClassifier (training) : {model_cbc.score(X_train, y_train)}")

# model_mpl = MLPClassifier()
# model_mpl.fit(X_train, y_train)
# print(f"MPL (testing) : {model_mpl.score(X_test, y_test)}")
# print(f"MPL (training) : {model_mpl.score(X_train, y_train)}")

pkl.dump(model_Log, open('model/model.pkl', 'wb'))