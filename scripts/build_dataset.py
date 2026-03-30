import sys
import os

# adiciona a pasta raiz do projeto ao caminho
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from src.normalizer import normalizar_texto

# Carregar o dataset original
df = pd.read_parquet("data/raw/olid_br/train.parquet")

print("Dataset carregado!")

# Criar nova coluna com texto normalizado
df["text_normalizado"] = df["text"].apply(normalizar_texto)

print("Normalização concluída!")

# Salvar novo dataset
df.to_parquet("data/processed/train_normalizado.parquet")

print("Dataset salvo em data/processed/")