n=int(input())
largest=0
s_lrgst=0
while n>0:
    d=n%10
    if largest <= d:
        s_lrgst=largest
        largest=d
    elif s_lrgst<=d:
        s_lrgst=d
    n//=10
print(s_lrgst)