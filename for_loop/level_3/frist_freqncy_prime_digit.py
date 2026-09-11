n=int(input())
freq=[0]*10

for i in str(n):
    dgt=int(i)
    freq[dgt]+=1
high=-1
res=-1
for dgt in range(10):
    if dgt<=1:
        continue
    is_prime=True
    for k in range(2,dgt):
        if dgt%k==0:
            is_prime=False
            break
    if is_prime and freq[dgt]!=0:
        if freq[dgt]>high:
            high=freq[dgt]
            res=dgt
print(freq)
if res==-1:
    print("No prime digit.")
else:
    print(res)