n=int(input())
smallest=float('inf')
for i in str(n):
    dgt=int(i)
    if dgt<smallest:
        smallest=dgt
print(smallest)
        