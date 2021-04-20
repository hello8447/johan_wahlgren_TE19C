# 1c
import pandas as pd

df = pd.read_csv("sysselsattning.csv", encoding="ISO-8859-1", header=1)
df_F = df[df["sysselsättning"] == "ej förvärvsarbetande"] 

plt.subplot(1,2,2)
label = ["ej förvärvsarbetande", "förvärsarbetande"]
values = [df_F["2019"].sum(), df["2019"].sum() - df_F["2019"].sum()]
plt.pie(values, labels=label)
plt.title("Andel förvarbetande/ej förvärvsarbetande")

