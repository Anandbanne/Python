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
        print(f"{i} is {freq[i]}")
