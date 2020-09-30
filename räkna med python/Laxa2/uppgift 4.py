#uppgift 4

vinkel = float(input("välj en vinkel: "))

if vinkel < 90:
    print("det är en spetsig vinkel")

elif vinkel == 90:
    print("det är en rät vinkel")

elif vinkel < 180:
    print("det är en trubbig vinkel")

elif vinkel == 180:
    print("det är en rak vinkel")

elif vinkel < 360 :
    print("det är en konvex vinkel")

elif vinkel == 360 :
    print("det är en hel vinkel")

else:
    print("vinkeln var mer än ett varv")