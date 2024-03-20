import math
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from dotenv import load_dotenv
load_dotenv()
train_data_path = os.getenv("HOUSING_TRAIN")
test_data_path = os.getenv("HOUSING_TEST")

# Read the data
X_full = pd.read_csv(train_data_path, index_col='Id')
X_test_full = pd.read_csv(test_data_path, index_col='Id')

# Obtain target and predictors
y = X_full.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = X_full[features].copy()
X_test = X_test_full[features].copy()

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

# Print the first several rows of training data:
print(X_train.head())

# define 5 random forest models:
model_1 = RandomForestRegressor(n_estimators=50, random_state=0)
model_2 = RandomForestRegressor(n_estimators=100, random_state=0)
model_3 = RandomForestRegressor(n_estimators=100, criterion='absolute_error', random_state=0)
model_4 = RandomForestRegressor(n_estimators=200, min_samples_split=20, random_state=0)
model_5 = RandomForestRegressor(n_estimators=100, max_depth=7, random_state=0)

models = [model_1, model_2, model_3, model_4, model_5]

# define a function that returns the MAE from the validation set:
def score_model(model, X_t, X_v, y_t, y_v):
  model.fit(X_t, y_t)
  preds = model.predict(X_v)
  return mean_absolute_error(y_v, preds)

best_model = "Model_0"
min_MAE = math.inf

for i in range(0, len(models)):
  mae = score_model(models[i], X_train, X_valid, y_train, y_valid)
  if mae < min_MAE:
    min_MAE = mae
    best_model = "Model_%d" % (i+1)
  print("Model_%d's MAE: %d" % (i+1, mae))

print("Best Model is: " + best_model)