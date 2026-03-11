import numpy as np
arr = np.random.normal(loc=50,scale=5,size=1000)
print(arr)
print("Mean: ",arr.mean())
print("Median: ",np.median(arr))
print("Standard Deviation: ",arr.std())
print("Variance: ",arr.var())
print("25th percentile",np.percentile(arr,25))
print("75th percentile",np.percentile(arr,75))