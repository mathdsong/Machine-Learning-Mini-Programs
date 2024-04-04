import pandas as pd
df = pd.Series([1,2,3,4,5])
df1 = pd.Series([1,2,3,4,5], index=['a','b','c','d','c'])
print(df)

#train a regression model
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
# generate a regression dataset
X, y = make_regression(n_samples=100, n_features=2, noise=0.1, random_state=1)
# fit our final model
model = LinearRegression()
model.fit(X, y)
# create new unknown instances
Xn, _ = make_regression(n_samples=3, n_features=2, noise=0.1, random_state=1)
# make some predictions
yn = model.predict(Xn)
# show the inputs and predicted outputs
for i in range(len(Xn)):
    print("X=%s, Predicted=%s" % (Xn[i], yn[i]))


