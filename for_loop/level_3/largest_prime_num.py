n=int(input())
lrgst_prime=0

for i in range(2,n+1):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        if lrgst_prime<i:
            lrgst_prime=i
print(lrgst_prime)