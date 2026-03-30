import pandas as pd

train = pd.read_parquet("data/raw/olid_br/train.parquet")

print("\nTotal de comentários:")
print(len(train))

print("\nDistribuição de ofensividade:")
print(train["is_offensive"].value_counts())

print("\nComentários ofensivos:")
offensive = train[train["is_offensive"] == "OFF"]
print(len(offensive))

print("\nTipos de ofensa:")

columns = [
    "racism",
    "sexism",
    "lgbtqphobia",
    "religious_intolerance",
    "xenophobia",
    "insult"
]

for col in columns:
    print(col, ":", train[col].sum())

print("\nExemplos de comentários ofensivos:\n")
print(train[train["is_offensive"] == "OFF"]["text"].head(10))