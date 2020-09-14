g =9.82

m = float(input("Hur mycket väger du? "))

F = m*g 

print(f"Din tyngdkraft är {F}N")

decimaltal = float(input("ange ett decimaltal:" ))

procent = decimaltal*100

print(f"{decimaltal} = {procent:.0f}%")

print(decimaltal,"=",round(procent),"%")

K= float(input("hur många K? "))

C=K-273.15

print(f"Det är {C}")

C= float(input("hur många c?"))

K=C+273.15

print (f"det är{K}")

engångsbiljett = 30 

månadskort = 775

antal = int(input("hur många gånger vill du åka västrafik?"))

kostnad =float(antal * engångsbiljett)

print (f"De blir sammanlagt {kostnad} kronor")

if kostnad > månadskort :

    print(f"det blir billigare med månadskort för {månadskort} kronor")

else:
    print("det lönar sig inte med månadskort")





