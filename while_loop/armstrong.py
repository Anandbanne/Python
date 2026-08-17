n=int(input())
temp=n
original =n
d_count=0
while temp >0:
    d_count+=1
    temp//=10

armstrong=0
while n>0:
    d=n%10
    armstrong+=d**d_count
    n//=10
if original==armstrong:
    print(f"the given {original} is armstrong")
else:
    print("not arm strong")
