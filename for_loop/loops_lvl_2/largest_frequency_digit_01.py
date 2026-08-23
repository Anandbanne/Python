n=int(input())
freq=[0]*10
for i in str(n):
    dgt=int(i)
    freq[dgt]+=1
print(freq)
l_f=0
f_d=-1
for i in range(10):
    if freq[i]>l_f:
        l_f=freq[i]
        f_d=i
print(f_d)
