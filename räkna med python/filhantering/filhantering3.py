
import matplotlib.pyplot as plt

def readAndDisplay(fname, gradePie):            # fname är filnamn och gradePie är en axes
    label = []                                  # label är ettiketterna till pajdelerna, init till tomt
    perc = []                                   # perc är pajdelernas storlekar init tomt
    with open(fname, "r") as resFile:           # öppnar filen 
        for rad in resFile:                     # loopar där rad tilldelas varje textrad i filen
            wordList = rad.split()              # delar upp raden till en lista av strängar 
            percStr = wordList[1][:-2]          # tar utden andra strängen på listan och kapar av de två sista tecknen
            label.append(wordList[0])           # adderar den första strängen på listn till label listan 
            perc.append(float(percStr))         # aderar procenttalet i perc listan
                                                # loopar runt
                                        
        resFile.close()                         # stänger ner filen
        gradePie.pie(perc, None, label)         # programmet skapar ett cirkel diagram
        gradePie.axis("equal")                  # gör så att det blir runda pajer
        gradePie.title.set_text(fname)          # Sätt filnamnet som titel
                                                # Funktionen är klar och kommer returnera

fig, (gradePieA, gradePieC) = plt.subplots(2)   # skapar två stycken subplots
fig.suptitle("Betygspajer")                     # sätter titeln
readAndDisplay("NPvt19MA2A.txt", gradePieA)     # behadlar första diagremmet
readAndDisplay("NPvt19MA2C.txt", gradePieC)     # behandlar andra diagremmet
plt.show()                                      # man visar diagremmen
