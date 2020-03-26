def getdigitcount(n):
    l=0;
    t=n;
    while(t>0):
        l=l+1
        t=t//10
    return l

def getarmstrong(n):
    l=getdigitcount(n)
    s=0;t=n;
    while(t>0):
        s = s+pow(t%10,l)
        t=t//10
    return s

for i in range(100,1000,1):
    n = i;
    #print("The Armstrong number of",n,"is",getarmstrong(n))
    armst = getarmstrong(n)
    if(armst==i):
        print("The number",armst,"is armstrong")

