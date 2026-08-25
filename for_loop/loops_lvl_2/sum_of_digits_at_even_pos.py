n=int(input())
pos=1
res=0
for i in str(n):
    dgt=int(i)
    if pos%2==0:
        res+=dgt
    pos+=1
print(res)