def Midinterchange(a):
    l=len(a)
    mid=l/2
    temp=a[mid]
    a[mid]=a[mid-1]
    a[mid-1]=temp
    return a
a=[10,20,40,30,50,60]
l=len(a)
if(l%2==0):
    print(Midinterchange(a))
else:
    print("Interchange is not neccessary")
