n=int(input())
target=int(input())
res=0
while n>0:
    d=n%10
    if target!=d:
        res=(res*10)+d
    n//=10
res1=0
while res>0:
    d1=res%10
    res1=(res1*10)+d1
    res//=10
print(res1)
