def interchangepos(a,p1,p2):
    temp=a[p1-1]
    a[p1-1]=a[p2-1]
    a[p2-1]=temp
    return a
a=[5,2,3,4,1]
print(interchangepos(a,2,4))