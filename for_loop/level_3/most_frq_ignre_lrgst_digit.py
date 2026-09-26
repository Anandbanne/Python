n=int(input())
freq=[0]*10
lrgst_dgt=-1
for i in str(n):
    dgt=int(i)
    if dgt>lrgst_dgt:
        lrgst_dgt=dgt
    freq[dgt]+=1
print(lrgst_dgt)
print(freq)
mst_frq=0
frq_n=-1
for j in range(10):
    if j==lrgst_dgt:
        continue
    if freq[j]>mst_frq:
        mst_frq=freq[j]
        frq_n=j
print(frq_n)