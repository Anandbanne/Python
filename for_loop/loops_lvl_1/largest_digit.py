n=int(input())
largest=0
for i in str(n):
    dgt=int(i)
    if largest<dgt:
        largest=dgt
print(largest)