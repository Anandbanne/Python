n=int(input())
largest=-1
for i in str(n):
    dgt=int(i)
    if dgt<=1:
        continue
    is_prime=True
    for j in range(2,dgt):
        if dgt%j==0:
            is_prime=False
            break
    if not is_prime:   
        if dgt>largest:
            largest=dgt
if largest==-1:
    print("no composite digits")
else:
    print(largest)