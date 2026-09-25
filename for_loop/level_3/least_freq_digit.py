n=int(input())
lst=[0]*10
least=float("inf")
freq_n=-1
for i in str(n):
    dgt=int(i)
    lst[dgt]+=1

for j in range(10):
    if lst[j]<least and lst[j]!=0:
        least=lst[j]
        freq_n=j
print(freq_n)
