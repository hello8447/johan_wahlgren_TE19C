
'''
# provbetyg
x = poäng
A: x>60
B: 56-60
c: 51-55
d: 41-50
e: 31-40
f: x<30
'''
import random as rnd 
# slumpar ett heltal mellan 0-65
poäng = rnd.randint(0,65)
# skapar en lista som håller 6 strangar
klass = ["kokchun", "Tommy","Tatiana", "Herman", "Henrik", "Zsofia","simon"]

if poäng <=30:
    betyg = "f"
elif poäng <=40:
    betyg = "e"
elif poäng <=50:
    betyg = "d"
elif poäng <=55:
    betyg = "c"
elif poäng <= 60:
    betyg = "b" 
else: 
    betyg = "a"

print (f"poäng {poäng}")
print (f" betyg{betyg}")