n=int(input())
freq=[0]*n+1
max_div=-1
dgt=-1
for i in range(1,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    freq[i]=count
print(freq)
for k in range(n+1):
    if freq[k]>max_div:
        max_div=freq[k]
        dgt=k
print(max_div)
print(dgt)
