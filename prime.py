import math
def isprime(n):
    sqrtn = int(math.sqrt(n))
    prime = True
    for i in range(2,sqrtn+1):
        if(n%i==0):
            prime = False
    return prime

n = 15
if(isprime(n)):
    print(n,"is prime number")
else:
    print (n,"is composite number")
