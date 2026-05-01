names=["A","B","C","D","E"]
age=[23,32,45,12,33]
res=list(zip(names,age))
res1=sorted(res,reverse=True)
p=1
for i in res1:
    print(f"{p}.{i[1]} age is {i[0]}")
    p=p+1