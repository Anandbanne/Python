n=int(input())
temp=n
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
count=0
while temp>0:
    d=temp%10
    count+=d
    temp//=10
if is_prime==True and count%2==0:
    print(f"{n} is super prime")
elif is_prime:
    print(f"{n} is prime")
else:
    print("Not prime")
