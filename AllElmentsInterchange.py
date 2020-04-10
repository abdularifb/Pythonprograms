def ElementsInterchange(a,l):
    if(l%2==0):
        print("Even Elements Intechange")
        for i in range(0,l,2):
            if(l-1==i):
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp
            else:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
    else:
        print("Odd Elements Interchange")
        for i in range(0,l,2):
            if(l-1==i):
                 []
            else:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
    return a
a=[10,20,30,40,50,60,70,80]
l = len(a)
print(ElementsInterchange(a,l))