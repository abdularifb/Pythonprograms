print("Find the odd numbers")
a=[20,7,6,3,5,8,2,7,10]
c=list(filter(lambda n:n%2!=0,a))
print c
print("Count the Odd Numbers")
count=0
for w in c:
    count=count+1
print count