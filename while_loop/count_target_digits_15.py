n=int(input())
count=0
t=int(input())
while n>0:
    d=n%10
    if d==t:
        count+=1
    n//=10
print(count)