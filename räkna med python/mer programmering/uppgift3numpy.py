# uppgift 3
import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(0,10)       # skapar definionsmängder
def f(x):                   # skapar en funktion
    y = 3*x+1               # skapar själva funktionen i y-axeln
    return y                # returnerar svaren

plt.plot(x,f(x))           # den plottar ut svaren man fick i den förra delen
plt.title("y = 3x+1")      # lägger till en titel
plt.xlabel("x")            # Namnger x-axeln till x
plt.ylabel("y")            # namnger y-axeln till y
plt.show()                 # ritar ut grafen