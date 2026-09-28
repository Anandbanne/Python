n=int(input())
add=0
count=0
for i in range(2,n+1):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        add+=i
        count+=1
print(add)
print(count)