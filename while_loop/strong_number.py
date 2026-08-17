n=int(input())
original=n
total=0
while n>0:
    d=n%10
    fact=1
    i=1
    while i<=d:
        fact*=i
        i+=1
    total+=fact
    n//=10
if total==original:
    print(f" {original} is strong number")
else:
    print("not strong")
