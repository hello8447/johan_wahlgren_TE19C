            #2a
with open("Provresultat.txt","r") as f1: # öppnar filen med f1
    for rad in f1:                       # loopar genom varje textrad i filen med rad
        print(rad)                       # skriver ut innehållet i textfilen
