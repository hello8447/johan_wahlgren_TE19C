            #2b
with open("Provresultat.txt","r") as provfil:   # öppnar filen med provfil
    elever = provfil.readlines()                # läser genom alla textraderna i en lista 
    elever.sort()                               # sorterar listan 
    print(elever)                               # printar listan
        
        

        