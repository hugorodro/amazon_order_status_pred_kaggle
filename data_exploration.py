import numpy as np
import pandas as pd


data= pd.read_csv("orders_data.csv")
data_arr = data.values

print(data_arr[0])