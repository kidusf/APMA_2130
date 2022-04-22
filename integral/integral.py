import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(start=0, stop=2, num=21)
h=np.array([0, 0.0854, 0.1425, 0.1779, 0.1927, 0.1921, 0.1801, 0.1604, 0.1361, 
0.11, 0.084, 0.0597, 0.0381, 0.0198, 0.005, -0.0062, -0.0141, -0.0191, -0.0217, -0.0223, -0.0214])
y=[]
for times in range(len(t)):
    sum=0
    for elements in range(times+1):
        sum=sum+(h[elements]*np.cos(t[times]-2*t[elements]))*0.1
    print(t[times], sum)
    y.append(sum)
plt.plot(t, np.array(y))
plt.title("Output of Convolution Integral")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.show()
      


    
