n=int(input())
res=0
while n>0:
    a=n%10
    res=(res*10)+a      #seperate the last digit from number
    n=n//10             #remove the last digit
print(res)