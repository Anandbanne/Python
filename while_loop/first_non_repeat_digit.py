n=int(input())
temp=n
original=n
count=0
while temp>0:
    count+=1
    temp//=10    
div=10**(count-1)
temp=n
freq=[0]*10
while div>0:
    d=temp//div
    freq[d]+=1
    temp%=div
    div//=10
print(freq)
div=10**(count-1)
found=False
while div>0:
    d=original//div
    if freq[d]==1:
        print(f"non repeate digit is {d}")
        found=True
        break
    original%=div
    div//=10
if not found:
    print("no non repeat digit.")
