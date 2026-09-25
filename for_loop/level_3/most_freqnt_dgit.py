n=int(input())
lst=[0]*10
largest=0
freq_n=-1
for i in str(n):
    dgt=int(i)
    lst[dgt]+=1

for j in range(10):
    if lst[j]>largest:
        largest=lst[j]
        freq_n=j
print(freq_n)