n=int(input())
found=True
if n<=1:
    found=False
else:
    for i in range(2,n):
        if n%i==0:
            found=False
            break
if found:
    print(f"{n} is prime.")
else:
    print(f"{n} not prime.")
