import pandas as pd
import matplotlib.pyplot as plt 
df = pd.read_csv("sysselsattning.csv", encoding="ISO-8859-1", header=1)

label = ["män", "förvärvsarb män", "kvinnor", "förvärvsarb kvinnor"]
df_M = df[df["kön"] == "män"]
df_K = df[df["kön"] == "kvinnor"]
df_AM = df_M[df_M["sysselsättning"] == "förvärvsarbetande"]
df_AK = df_K[df_K["sysselsättning"] == "förvärvsarbetande"]
values = [df_M["2019"].sum(), df_AM["2019"].sum(), df_K["2019"].sum(), df_AK["2019"].sum()] 

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(label, values)
plt.show()