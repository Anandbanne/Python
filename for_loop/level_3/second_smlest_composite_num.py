n=int(input())
smallest=float("inf")
s_smallest=float("inf")
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
            s_smallest=smallest
            smallest=dgt
        elif dgt!=smallest and dgt<s_smallest:
            s_smallest=dgt
if s_smallest==float("inf"):
    print("no s_smalllest composite digit")
else:
    print(s_smallest)