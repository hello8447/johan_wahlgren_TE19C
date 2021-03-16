#uppgift 2
import random
import random as rnd
kast = {}               # skapar en tomt dictionary
for i in range (1,7):   # loopar talen mellan 1 och 6
  kast[f"{i}"] = 0      # nollställer kast dictionaryt
for i in range(100000): # loopar 100000 tal 
  tärningskast = random.randint(1,7)    #slumpar tärningskast
  if tärningskast == 1: #ifall tärningen är ett
    kast["1"] += 1      # ska man addera till 1 kategoriet
  if tärningskast == 2:
    kast["2"] += 1
  if tärningskast == 3:
    kast["3"] += 1
  if tärningskast == 4:
    kast["4"] += 1
  if tärningskast == 5:
    kast["5"] +=1
  if tärningskast == 6:
    kast["6"] += 1
print(kast)