n=int(input())
found=False
for i in str(n):
    dgt=int(i)
    if dgt<=1:
        continue
    is_prime=True
    for j in range(2,dgt):
        if dgt%j==0:
            is_prime=False
            break
    if not is_prime:
        print(dgt)
        found=True
        break
if not found:
    print("no composite numbers")
