n=int(input())
original=n
res=''
for i in str(n):
    res=i+res
res=int(res)
if res==original:
    print(f"{original} palindrome")
else:
    print("not palindrome")