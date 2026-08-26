n=int(input())
original=int(n)
count=0
for i in str(n):
    count+=1
total=0
for i in str(n):
    dgt=int(i)
    total+=(dgt**count)
if total==original:
    print(f"{n} is armstrong")
else:
    print("not armstrong")
