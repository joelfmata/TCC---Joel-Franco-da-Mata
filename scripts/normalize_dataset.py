import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.normalizer import normalizar_texto

df = pd.read_csv("data/processed/youtube_abbrev.csv")

df["text_normalized"] = df["text"].apply(normalizar_texto)

df.to_csv("data/processed/youtube_normalized.csv", index=False)

print("Dataset normalizado!")