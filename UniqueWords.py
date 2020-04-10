def GetUnique(str):
    lst = str.split()
    print lst
    res=[]
    for w in lst:
        if w not in res:
            res.append(w)
    return res
str="I am arif I am Software Engineer"
print(GetUnique(str))