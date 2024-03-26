import os
import pandas as pd
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from sklearn import linear_model
load_dotenv()
bmi_path = os.getenv("BMI")

df = pd.read_csv(bmi_path, index_col=0)
print("*********** Data Frame ***********")
print(df)
print("*********** sum ***********")
print(df.sum())
# print("*********** average ***********")
# print(df.sum() / df.shape[0])
print("*********** mean, median, std ***********")
print(df.describe())
print("*********** mode ***********")
print(df.mode())
print("*********** variance ***********")
print(df.var())


# print("*********** plot ***********")
plt.scatter(df['height'], df['weight'], color = 'green')
plt.axis([3.6, 6.8, 112, 226])
plt.xlabel('height in feet')
plt.ylabel('weight in lbs')
# create linear regression object
lr = linear_model.LinearRegression()
lr.fit(X=df[['height']], y=df[['weight']])
# make prediction
pred_weight = lr.predict(df[['height']])
plt.plot(df['height'], pred_weight, color='blue')

plt.show()
