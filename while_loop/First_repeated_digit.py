n=int(input())
temp=n
count=0
while temp>0:
    count+=1
    temp//=10
div=10**(count-1)

#print(count)
#print(div)

seen=[False]*10
found=False
while div>0:
    d=n//div
    n%=div
    if seen[d]:
        found=True
        print(f"First repeat digit is {d} ")
        break
    seen[d]=True
    div//=10
if not found:
    print("no repeated digit")