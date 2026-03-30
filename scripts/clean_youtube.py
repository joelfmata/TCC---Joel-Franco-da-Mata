import pandas as pd
import re

def limpar_texto(texto):
    texto = str(texto).lower()

    # remover links
    texto = re.sub(r"http\S+", "", texto)

    # remover caracteres especiais
    texto = re.sub(r"[^a-zA-Zà-úÀ-Ú0-9\s]", "", texto)

    # remover espaços duplicados
    texto = re.sub(r"\s+", " ", texto)

    return texto.strip()

df = pd.read_csv("data/raw/youtube_comments.csv")

df["text"] = df["text"].apply(limpar_texto)

df = df[df["text"].str.len() > 3]

df.to_csv("data/processed/youtube_clean.csv", index=False)

print("Comentários limpos!")