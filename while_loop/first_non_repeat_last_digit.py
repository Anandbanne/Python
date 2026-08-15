n=int(input())
temp=n
freq=[0]*10
while temp>0:
    d=temp%10
    freq[d]+=1
    temp//=10
found=False
while n>0:
    d=n%10
    if freq[d]==1:
        print(f"non repeat last digit is {d}")
        found=True
        break
    n//=10
if not found:
    print("no non repeat digit")
