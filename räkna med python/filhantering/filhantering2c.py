Alist = []                                                 # skapar tomma betygs listor
Blist = []
Clist = []
Dlist = []
Elist = []
Flist = []
with open("Provresultat.txt","r") as resFil:                # öppnar textfilen som esFil
    for rad in resFil:                                      # loopar genom alla textrader med rad
        rad = rad.rstrip()                                  # tar bort blanktecken och sånt
        wordList = rad.split()                              # spliitar orden till en lista 
        points = int(wordList[len(wordList) - 1])           # man tar siffrorna från listan
        if points < 20:                                     # kontrelerar hur många poäng man får och adderar till rätt betygslista
            Flist.append(rad)                               
        elif points < 30:                                  
            Elist.append(rad)                              
        elif points < 40:
            Dlist.append(rad)
        elif points < 50:
            Clist.append(rad)
        elif points < 60:
            Blist.append(rad)
        else:
            Alist.append(rad)
                                                            # loopar runt
    resFil.close()                                          # stänger ner filen
    print("F")                                              # printar ut betyget som rubrik 
    for i in range(len(Flist)):                             # skriver ut alla i listan
        print(Flist[i])
    print("E")
    for i in range(len(Elist)):
        print(Elist[i])
    print("D")
    for i in range(len(Dlist)):
        print(Dlist[i])
    print("C")
    for i in range(len(Clist)):
        print(Clist[i])
    print("B")
    for i in range(len(Blist)):
        print(Blist[i])
    print("A")
    for i in range(len(Alist)):
        print(Alist[i])       
