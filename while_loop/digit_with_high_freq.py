n=int(input())
frequency=[0]*10
while n>0:
    d=n%10
    frequency[d]+=1
    n//=10
print(frequency)
highest=0
answer=0
for i in range(10):
    if frequency[i]>highest:
        highest=frequency[i]
        answer=i
print(answer) 