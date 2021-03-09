import random 
# 1a
with open("tärningskast.txt", "w") as f1:       # Öppnar filen som f1
    f1.write("Simulera 10 tärningskast [")      # skriver rubrik till textfilen 
    dice = []                                   # dice är listan som är tom
    for i in range(10):                         # looopar runt tio gånger 
        dice.append(random.randint(1,6))        # lägg till tärningskasten till dice listan
        f1.write(str(dice[i]))                  # skriver ner tärningskastet på textfilen
        if i != 9:                              # ska inte ha ett komma efter sista siffran
            f1.write(",")                       # men övriga måste ha ett komma efter sig
    f1.write("]\n")                             # när man har loopat klart ska man addera en slut lista och ny rad
    # 1b och c
    dice.sort()                                 # sorterar listan i a uppgiften
    femmor = 0                                  # nollställer fem räknaren
    f1.write("Kastet sorterat: [")              # lägge till en rubrik på textfilen
    for i in range(10):                         # ska loopa tio gånger
        f1.write(str(dice[i]))                  # ska addera tärningskasten till textfilen
        if dice[i] == 5:                        # ifall tärningen är fem 
            femmor += 1                         # ska man addera en till fem räknaren (för att det behövs inför nästa uppgift) 
        if i != 9:                              # Ska inte ha ett komma efter sista siffran
            f1.write(",")                       # men övrigt måsta man ha ett komma efter sig
    f1.write("]\n")                             # när man har loopat klart ska man addera en slut lista och ny rad                     
    
    f1.write("Antalet femmor: " )               # skriver rubriken på textfilen
    f1.write(str(femmor))                       # skriver ner hur många femmor man fick
    f1.write("\n")                              # ny rad

    f1.close()                                  # stänger ner filen

