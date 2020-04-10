def stretch(str,rl,indices):
    el=rl-len(str)

    if(el<0):
        return []
    elif(el==0):
        return [].append(str)
    result=[]
    for i in range(len(str)):
        for j in range(1,el+1):
            for m in range(i,len(str)):
                tres=(str[:m] + str[m]* (el-1) + str[m:])
                tres1 =[x for x in tres]
                tres1.insert(i,str[i])
                res=("".join(tres1))
                if res not in result:
                     result.append(res)
    result.sort()
    if indices==[]:
        return result
    finalresult=[]
    for x in indices:
        finalresult.append(result[x])
    return finalresult
s="1234"
rl=6
ind=[1,2,3]
res=stretch(s,rl,ind)
for x in res:
    print(x)
