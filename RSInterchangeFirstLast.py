def Reversestring(st):
    a=st.split(" ")
    rev=a[-1::-1]
    rs=" ".join(rev)
    print rs
    l=len(rev)
    ra=""
    for i in range(0,l):
        str=rev[i]
        ra= ra+str[-1:]+str[1:-1]+str[:1]+" "
    return ra
print(Reversestring("Ramu is my friend"))