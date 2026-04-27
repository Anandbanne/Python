a=input("Enter the Voter Name: ")
b=input("Gender: ")
c=int(input("Age: "))
if c>18 and b=="F":
    print(f"{a} is right to vote.")
elif c>30 and b=="M":
    print(f"{a} is right to vote.")
else:
    print(f"{a} Not Eligible")     
    