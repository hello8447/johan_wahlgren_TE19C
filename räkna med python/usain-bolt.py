import matplotlib.pyplot as plt 
s = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] #lista som håller sträckan
t = [1.83, 2.87, 3.78, 4.65, 5.5, 6.32, 7.14, 8.79, 9.69]
v=[0] #tom lista


for i in range (1, len(t)):
    v_i = (s[i]- s[i-1])/(t[i]-t[i-1])
    v.append()
