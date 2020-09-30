def primtal(tal) :
    for i in range(2,tal-1) :
        if (tal % i) == 0 :
            return False
    return True

for x in range (1,100) :
    if primtal(x) :
        print(x)



