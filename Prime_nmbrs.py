a=int(input("Enter the Number: "))
c=0
for i in range(2,a):
    if a%i==0:
        c=c+1
if c==0:
    print("it is prime nmbr.")
else:
    print("it is composite nmbr.")        