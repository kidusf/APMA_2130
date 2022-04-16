import numpy as np


t=np.linspace(start=0, stop=2, num=21)
h=np.array([0, 0.0854, 0.1425, 0.1779, 0.1927, 0.1921, 0.1801, 0.1604, 0.1361, 
0.11, 0.084, 0.0597, 0.0381, 0.0198, 0.005, -0.0062, -0.0141, -0.0191, -0.0217, -0.0223, -0.0214])
count=0
sum=0
for elements in t:
    sum=sum+(h[count]*np.cos(2*elements))*0.1
    count+=1
print(sum)
    
