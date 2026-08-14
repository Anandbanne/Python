n=int(input())
largest=0
while n>0:
    a=n%10
    if largest<=a:
        largest=a
    n//=10
print(largest)
        