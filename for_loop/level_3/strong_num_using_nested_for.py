n=int(input())
res=0
for i in str(n):
    dgt=int(i)
    fact=1
    for j in range(1,dgt+1):
        fact*=j
    res+=fact
if res==n:
    print(f"{n} is strong number.")
else:
    print(f"{n} is not strong number.")    