#triangelns vinkel
#*spetsig
#*trubbig
#*rät
#*annat

vinkel = float(input("ange en vinkel v i grader, där 0 <= 360 "))

if vinkel >= 0 and vinkel <90 :
    print("vinkeln är spetsig")
elif vinkel > 90 and vinkel < 180:
    pass
else: 
    print("vinkeln är inte spetsig, trubbig eller rät")