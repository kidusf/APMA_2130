import matplotlib.pyplot as plt
import numpy as np
import math

x0=float(input("x0= "))
y_m=float(input("y0= "))
x=np.linspace(start=-100, stop=100, num=1000)
y=np.linspace(start=-100, stop=100, num=1000)
x_final=float(input("Enter point of approximation: "))
dx=float(input("Enter step size: "))
measured_x=[]
measured_y=[]
while(x0<=x_final):
    #differential equation
    dy_dx=0.8*y_m
    measured_x.append(x0)
    measured_y.append(y_m)
    print(x0, y_m, dy_dx)
    y_m=dy_dx*dx+y_m
    x0+=dx
plt.plot(np.array(measured_x), np.array(measured_y), marker="o")
plt.show()


    
    