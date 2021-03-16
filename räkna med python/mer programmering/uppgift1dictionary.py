# uppgift 1
kurser = dict (
  programmering = 100,        # ger kuserna poäng
  engelska = 100,       
  matte = 100,
  idrott = 50,
  fysik = 150,
  webbutveckling = 100,
  daodac = 100,
  svenska = 100,
)
if key in kurser:           # skapar en if-sats till kurserna
  print("Den totala poängen är:", sum(kurser.values())) # man beröknar summan av alla kuserna och sedan printar man ut det