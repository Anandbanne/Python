n=int(input())
target=int(input())
temp=n
count=0
while temp>0:
    d=temp%10
    count+=1
    temp//=10
div=10**(count-1)
res=0
while n>0:
    d=n//div
    n%=div
    if target!=d:
        res=res*10+d
    div//=10
print(res)
