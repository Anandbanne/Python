n=int(input())
total=0
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
        total+=dgt
print(total)