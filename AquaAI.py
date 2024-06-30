import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv("Water_Quality_Testing(in).csv")
y = np.array(df['Safe'])
X = np.array(df.drop(columns = 'Safe'))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)
log_reg = LogisticRegression(random_state = 0, C = 100, max_iter = 10000).fit(X_train, y_train)

#input = np.array([[1.23, 2, 3, 4, 5, 6]])

print(input)

prediction = log_reg.predict(input)

score = log_reg.score(X_test, y_test)

conf = log_reg.predict_proba(input)

print(conf[0][prediction[0]])

print(prediction[0])

pickle.dump(log_reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))

#4.29, 23.3, 3.4, 9.5, 351, 158.73