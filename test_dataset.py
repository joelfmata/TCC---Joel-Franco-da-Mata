import pandas as pd

train = pd.read_parquet("data/raw/olid_br/train.parquet")
test = pd.read_parquet("data/raw/olid_br/test.parquet")

print(train.head())
print(train.columns)
print("Total train:", len(train))