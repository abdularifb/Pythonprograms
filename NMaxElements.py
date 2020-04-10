def NMax(a,n):
    b=a[:]
    b.sort(reverse=True)
    m=b[:n]
    return m
a=[1,2,3,5,7,1.5,10,16]
n=3
print(NMax(a,n))

