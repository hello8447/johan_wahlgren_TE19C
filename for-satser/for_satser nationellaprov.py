#fuska på nationella prov matte 3c

 # a= 5/(2+4/x)

a_vals = [ ]

for x in range(1,100):
    a = round(5*(2+4/x))
    a_vals.append(a)

print(a_vals)