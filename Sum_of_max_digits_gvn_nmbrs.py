a=int(input("Enter a number1: "))
b=int(input("Enter a number2: "))
c=int(input("Enter a number3: "))
a1=[int(i) for i in str(a)]
b1=[int(i) for i in str(b)]
c1=[int(i) for i in str(c)]
sum=max(a1)+max(b1)+max(c1)
print(sum)