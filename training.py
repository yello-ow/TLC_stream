from datetime import datetime 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics
import pickle

input_file = "./data/trips/yellow_tripdata_2021-01.csv"

df = pd.read_csv(input_file, header=0)
df = df.loc[(df["total_amount"] > 0) & (df["total_amount"] < 5000) & (df["trip_distance"] > 0) & (df["trip_distance"] < 500) & (df["passenger_count"] < 4)]
distance = df["trip_distance"]
hours = df["tpep_pickup_datetime"].map(
  lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S").hour
)
data = pd.concat([hours, distance], axis=1)
target = df["total_amount"]

train_x, test_x, train_y, test_y = train_test_split(
  data,
  target,
  test_size = 0.2,
  random_state = 24
)

lr = LinearRegression()
lr.fit(train_x, train_y)

prediction = lr.predict(test_x)

mse = metrics.mean_squared_error(test_y, prediction)
r2 = metrics.r2_score(test_y, prediction)
print(mse)
print(r2)
print("PREDICTION")
print(prediction[:5])
print("LABEL")
print(test_y[:5])

with open("model.pkl", "wb") as f:
  pickle.dump(lr, f)
