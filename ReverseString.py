def Reversestring(st):
    a=st.split(" ")
    rev=a[-1::-1]
    revstring=" ".join(rev)
    return revstring
print(Reversestring("Ramu is my friend"))