n=int(input())
smallest=float('inf')
while n>0:
    a=n%10
    if a<smallest:
        smallest=a
    n//=10
print(smallest)