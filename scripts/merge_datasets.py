import pandas as pd

# carregar OLID-BR
df_olid = pd.read_parquet("data/raw/olid_br/train.parquet")

print("OLID carregado:", len(df_olid))

# carregar seu corpus
df_abrev = pd.read_csv("data/raw/abreviacoes.csv")

print("Abreviações carregadas:", len(df_abrev))

# alinhar colunas (igualar ao OLID)
df_abrev["is_targeted"] = "UNT"
df_abrev["targeted_type"] = "NONE"

# juntar datasets
df_final = pd.concat([df_olid, df_abrev], ignore_index=True)

print("Dataset final:", len(df_final))

# salvar
df_final.to_parquet("data/processed/dataset_final.parquet")

print("Dataset final salvo!")