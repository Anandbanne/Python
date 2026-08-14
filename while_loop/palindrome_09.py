n=int(input())
orgnl=n
res=0
while n>0:
    a=n%10
    res=(res*10)+a
    n//=10
if orgnl==res:
    print(f'{orgnl} is palindrome')
else:
    print(f"{orgnl} is not palindrome" )