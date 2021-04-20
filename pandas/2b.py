#2b
import pandas as pd

df = pd.read_csv("sysselsattning.csv", encoding="ISO-8859-1", header=1)
df_M = df[df["kön"] == "kvinnor"]
df_F = df_M[df_M["sysselsättning"] == "förvärvsarbetande"]
print(df_F["2019"].sum()) 