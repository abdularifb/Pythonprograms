a = [10, 5, 50, 40, 4.0, 5.9, 100]
n = len(a)

# To find the Second smallest Element
def small(n,a):
    print("Find the Second Smallest element")
    for i in range(0, n):
        for j in range(i+1,n):
            if (a[i] > a[j]):
                temp=a[i]
                a[i] =a[j]
                a[j]=temp
    print a
    print("Thde second Smallest element is",a[1])

# To find Second Largest Element

def large(n,a):
    print("Find the Second Largest element")
    for i in range(0, n):
        for j in range(i+1,n):
            if (a[i] < a[j]):
                temp=a[i]
                a[i] =a[j]
                a[j]=temp
    print a
    print("Thde second Largest element is",a[1])

small(n,a)
large(n,a)




