n=int(input())
largest=-1
s_lrgst=-1
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
            s_lrgst=largest
            largest=dgt
        elif dgt>s_lrgst and dgt!=largest:
            s_lrgst=dgt
if s_lrgst==-1:
    print("No second largest composite digit.")
else:
    print(s_lrgst)