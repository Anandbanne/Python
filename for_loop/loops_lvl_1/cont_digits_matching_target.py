n=int(input())
target=int(input())
count=0
for ch in str(n):
    dgt=int(ch)
    if dgt==target:
        count+=1
print(count)
