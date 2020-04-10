def sortonsecond(l1,l2):

    z=zip(l2,l1)
    res = [x for _, x in sorted(z)]
    return res
l1=['a','b','c','d','e']
l2=[1,2,3,2,1]
print(sortonsecond(l1,l2))

