n=input()
total=0
for i in str(n):
    dig=int(i)
    if dig%2==0:
        total+=dig
print(total)
