a=int(input("Enter the number1: "))
b=int(input("Enter the number2: "))
while(b!=0):
    rem=a%b
    a=b
    b=rem
print(f"GCD: {a}")    