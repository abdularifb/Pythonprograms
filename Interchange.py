def interchange(a):
    al=len(a)
    temp=a[0]
    a[0]=a[al-1]
    a[al-1]=temp
    return a
a=[5,2,3,4,1]
print(interchange(a))