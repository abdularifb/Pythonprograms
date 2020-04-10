def PNL(a,n):
    b=a[:]
    b.sort()
    m=b[:n]
    print m
    product=1
    for w in m:
        product=product*w
    return product
a=[5,1,10,4,15,6]
n=3
print(PNL(a,n))

