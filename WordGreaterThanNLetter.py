def WordGreaterN(str,n):
    b=str.split(" ")
    res = [x for x in b if len(x)>n]

    for w in res:
        print w

(WordGreaterN("ramu is my friend",3))