n=int(input())
freq=[False]*10
res=0
for i in str(n):
    dgt=int(i)
    if freq[dgt]==False:  # or { if not freq[dgt]: } 
        freq[dgt]=True
        res=(res*10)+dgt
print(res)