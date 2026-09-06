n=int(input())
count=0
for i in str(n):
    dgt=int(i)
    if dgt<=1:
        count+=1
        continue
    found=True
    for j in range(2,dgt):
        if dgt%j==0:
            found=False
            break    
print(count)