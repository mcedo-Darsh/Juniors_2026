a,b = map(int,input("Enter 2 numbers: ").split())

for i in range(a,b+1):
    j=2
    isPrime = True
    while j*j<=i:
        if i%j==0:
            isPrime = False
            break
        j+=1
    if isPrime and i!=1:
        print(i)