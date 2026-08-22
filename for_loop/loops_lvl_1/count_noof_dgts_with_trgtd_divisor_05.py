n=int(input())
m=int(input())
count=0
for ch in str(n):
    dgt=int(ch)
    if dgt%m==0:
        count+=1
print(count)
