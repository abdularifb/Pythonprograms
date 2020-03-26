'''def fibo(n):
    a = 0
    b = 1

    if(n==0):
        return a
    elif(n==1):
        return b
    else:
        for i in range(2,n+1):
         c = a + b
         a = b
         b = c
    return c

n = int(input("Enter the n value:"))
print(n,"Fibonacci number is",fibo(n)) '''

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(6))


