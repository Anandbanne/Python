n=int(input())
temp=n
count=0
while temp>0:
    count+=1
    temp//=10
div=10**(count-1)
freq=[False]*10
res=0
while n>0:
    d=n//div
    if freq[d]!=True:
        freq[d]=True
        res=res*10+d
    n%=div
    div//=10
print(res)
