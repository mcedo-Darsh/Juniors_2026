import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(0,2*np.pi,31)
y = np.sin(x)
y=y*10+15
plt.plot(y,'')
plt.xlabel("Days")
plt.ylabel("Temperature( in Degree Celcius)")
plt.title("Temperature in January 2025")

rolling_avg = []

for i in range(6):
    rolling_avg.append(float((np.sum(y[0:i+1]))/(i+1)))

for i in range(6,31):
    rolling_avg.append(float((np.sum(y[i-6:i+1]))/(7)))

plt.plot(rolling_avg,'*')

print("Days when temp is above 20*C : ")

for i in range(31):
    if y[i]>20:
        print(i+1)

plt.show()