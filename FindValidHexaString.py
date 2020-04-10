def FindHexa(s):
    #find first test list
    alpha = "A"
    p = []
    t = []
    for i in range(0, 6):
        p.append(alpha)
        alpha = chr(ord(alpha) + 1)
    for k in range(0, 10):
        t.append(k)
    m = [str(char) for char in t]
    t1=p+m
    print t1

    #Find second test list

    t2 = [char for char in s]
    print t2
    l1=len(t1)
    l2=len(t2)



FindHexa("A")
