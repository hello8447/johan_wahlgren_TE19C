import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(-2,2)           # skapar definionsmängder
def f(x):                       # skapar en funktion
    y = x**2-1                  # skapar själva funktionen och ger värden till y-axeln
    return y                    # returnerar svaren till den förra delen

plt.plot(x,f(x))                # den plottar ut resultaten till den funktionen
plt.title("y = x**2-1")         # lägger till en titel
plt.xlabel("x")                 # namnger x-axeln till x
plt.ylabel("y")                 # namnger y-axeln till y
plt.show()                      # ritar ut grafen 