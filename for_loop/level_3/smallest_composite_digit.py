n=int(input())
smallest=float("inf")
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
        if dgt<smallest:
            smallest=dgt
if smallest==float("inf"):
    print("no composite digits")
else:
    print(smallest)