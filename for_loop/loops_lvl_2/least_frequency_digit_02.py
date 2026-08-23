n=int(input())
freq=[0]*10
for i in str(n):
    dgt=int(i)
    freq[dgt]+=1
print(freq)
s_f=float("inf")
f_d=-1
for i in range(10):
    if freq[i]<s_f and freq[i]!=0:
        s_f=freq[i]
        f_d=i
print(f_d)
