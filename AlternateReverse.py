def AlternateReverse(st,le):
    res="".join(char[1]+char[0] for char in zip(st[::2],st[1::2]))
    if(le%2==0):
        print res
    else:
        print res+st[-1]
st="malayala"
le=len(st)
AlternateReverse(st,le)
