#1b
import pandas as pd

df = pd.read_csv("sysselsattning.csv", encoding="ISO-8859-1", header=1)
df_F = df[df["sysselsättning"] == "ej förvärvsarbetande"] 
print(df_F["2019"].sum())