def FindNumerolgyNumber(l1,l2,a):
    l=len(a)
    sum=0
    for i in range(0, l):
        for le , ln in zip(l1,l2):
                if(le==a[i]):
                    sum=sum+ln
    if(sum>10 or sum<100):
        first = sum // 10
        last = sum % 10
        print first+last
    else:
        print sum

l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
l2 = [1, 2, 3, 4, 5, 8, 3, 5, 1, 1, 2, 3, 4, 5, 7, 8, 1, 2, 3, 4, 6, 6, 6, 5, 1, 7]
a = "india"
FindNumerolgyNumber(l1,l2,a)



    #print("letters :%s  Numbers:%d" %(le,ln))
