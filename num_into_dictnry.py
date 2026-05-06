a=2333311
b={}
for i in str(a):
    if i not in b:
        b[i]=1
    else:
        b[i]=b[i]+1
print(b)        