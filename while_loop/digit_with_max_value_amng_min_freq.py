n=int(input())
temp=n
freq=[0]*10
while temp>0:
    d=temp%10
    freq[d]+=1
    temp//=10
print(freq)
smallest=float("inf")
smallest_d=-1
for i in range(10):
    if freq[i]<=smallest and freq[i]!=0:
        smallest=freq[i]
        smallest_d=i
print(smallest_d)
