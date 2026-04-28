import random
p1=input("Enter the player1:")
p2=input("Enter the Palyer2:")
s1=10
s2=10
d1=random.randint(1, 10)
d2=random.randint(1, 10)
print(".....Player_1 turn.....")
while(True):
    g1=int(input("Enter the Number:"))
    s1=s1-1
    if d1==0:
        break
print(".....Player_2 turn.....") 
while(True):
    g2=int(input("Enter the Number:"))
    s2=s2-1
    if d2==0:
        break
print("...Summary...")
print(f"{p1} score is:{s1}")
print(f"{p2} score is: {s2}")
print("...Result...")
if s1>s2:
    print(f"{p1} is Winner")
elif s1<s2:
    print(f"{p2} is winner")
else:
    print("Tie")    