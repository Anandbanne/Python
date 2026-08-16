n=int(input())
temp=n
freq=[0]*10
largest=0
s_largest=0
while temp>0:
    d=temp%10
    freq[d]+=1
    temp//=10
largest_d=-1
s_largest_d=-1
for i in range(10):
    if freq[i]>largest:
        s_largest=largest
        s_largest_d=largest_d
        largest=freq[i]
        largest_d=i
    elif freq[i]>s_largest:
        s_largest=freq[i]
        s_largest_d=i
print(f"most frequent digit is {largest_d}")
if s_largest_d==-1:
    print("no second largest digit in number")
else:
    print(f"second most frequent digit is {s_largest_d}")
