n=int(input())
res=0
while n>0:
    a=n%10
    if a%2==0:
        res+=a
    n//=10
print(res)