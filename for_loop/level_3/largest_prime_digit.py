n=int(input())
largest=-1
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
        if largest<dgt:
            largest=dgt
if largest==-1:
    print("no prime digit.")
else:
    print(largest)