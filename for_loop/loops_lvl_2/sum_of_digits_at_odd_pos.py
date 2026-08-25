n=int(input())
res=0
pos=1
for i in str(n):
    dgt=int(i)
    if pos%2!=0:
        res+=dgt
    pos+=1
print(res)