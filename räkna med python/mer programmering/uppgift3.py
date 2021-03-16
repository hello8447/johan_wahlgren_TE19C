#uppgift 3
pokedex = {}        # skapar ett tomt dictionary
with open("pokemons.txt", "r") as dicfile:  # öppnar textfilen
    for pokeline in dicfile:            #loopar igenom dicfile med pokeline
        s = pokeline.split()            # delar upp pokeline innehållet till flera strängar
        dicStr = "Typ: " + s[2] +", index: " + s[0]    # bygger upp en sträng med typen och indexet på pokemonen  
        pokedex[s[1]] = dicStr       # man lägger key och value i dictionarityt
print(pokedex["Gastly"])        # väljer vilken pokemon man vill veta information om
print(pokedex["Pikachu"])
