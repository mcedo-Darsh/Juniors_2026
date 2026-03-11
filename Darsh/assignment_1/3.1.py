import numpy as np
import matplotlib.pyplot as plt

fig,(p1,p2,p3) = plt.subplots(1,3,figsize=(9,3))

xsq = np.linspace(-10,10,50)
ysq = xsq*xsq

p1.plot(xsq,ysq)
p1.set_title("X squared")

x=np.linspace(0,1,100)
y=np.random.normal(loc=0.5,scale=0.1,size=100)

p2.plot(x,y,color='green')
p2.set_title("Random")

rng = np.random.default_rng()
xa = rng.exponential(scale=1,size=500)
p3.hist(xa,color="red")
p3.set_title("Histogram")
plt.tight_layout()
plt.show()