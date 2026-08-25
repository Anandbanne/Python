n=int(input())
res=0
for i in str(n):
    dgt=int(i)
    if dgt%2==0:               
        res=(res*10)+dgt
print(res)