import pandas as pd
import numpy as np

data = pd.read_csv("cme/data.csv")
x = data[["customer_id", "transaction_id","contract_id"]].values
print(x)