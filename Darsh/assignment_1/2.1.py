import numpy as np
rg = np.random.default_rng()
A = rg.integers(1,11,9).reshape(3,3)
B = rg.integers(1,11,9).reshape(3,3)

print("A\n",A)
print("\nB\n",B)

print("\nA+B")
print(A+B)

print("\nA*B")
print(A*B)

print("\nA.B")
print(np.dot(A,B))

print("\ndet(A)")
print(int(np.linalg.det(A)))