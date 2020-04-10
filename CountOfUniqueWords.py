def GetUnique(str):
    lst = str.split()
    print lst
    res=[]
    for w in lst:
        if w not in res:
            res.append(w)
        else:
            count=1
            temp=count+1
            print("The word is:",w,"present",temp)
    return res
str="I am arif I am Software Engineer Engineer"
print(GetUnique(str))