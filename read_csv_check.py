# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv("data/vehicles_processed.csv", encoding="utf-8")
print(f"shape: {df.shape}")
print("colunas:", list(df.columns))
print("\ncontagem de nulos por coluna:")
print(df.isna().sum())
print("\nprimeiras 5 linhas:")
print(df.head(5).to_csv(index=False))
