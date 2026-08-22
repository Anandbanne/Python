fact=1
n=int(input())
for i in range(n,0,-1):
    fact*=i
print(f"{n}! is {fact}")
