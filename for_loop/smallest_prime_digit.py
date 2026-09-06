n=int(input())
smallest=float("inf")
for i in str(n):
    dgt=int(i)
    if dgt<=1:
        continue
    found=True
    for j in range(2,dgt):
        if dgt%j==0:
            found=False
            break
    if found:
        if smallest>dgt:
            smallest=dgt
if smallest==float('inf'):
    print("no prime digit.")
else:
    print(smallest)