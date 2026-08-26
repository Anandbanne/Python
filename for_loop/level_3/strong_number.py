#calculate factorial for each digit and sum. if it is equal to num. it is Strong
n=int(input())
original=n

total=0
for i in str(n):
    dgt=int(i)
    fact=1
    for j in range(1,dgt+1):       
        fact*=j
    total+=fact
if total==original:
    print(f"{n} is  strong number")
else:
    print("not strong number.")
