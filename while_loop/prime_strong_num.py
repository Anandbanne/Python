n=int(input())
is_prime=True
if n<=1:
    is_prime=False
else:
    i=2
    while i<n:
        if n%i==0:
            is_prime=False
            break
        i+=1
total=0
orginal=0
while n>0:
    d=n%10
    fact=1
    i=1
    while i<=d:
        fact*=i
        i+=1
    total+=fact
    n//=10
if total==orginal and is_prime:
    print("Strong prime")
elif is_prime:
    print("prime number")
else:
    print("only Strong")
