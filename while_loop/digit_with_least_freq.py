n=int(input())
freq=[0]*10
while n>0:
    d=n%10
    freq[d]+=1
    n//=10
print(freq) #print the list with digits

smallest=float('inf')
answer=0
for i in range(10):
    if freq[i]<smallest and freq[i]>0 :
        smallest=freq[i]
        answer=i
print(answer)