a=input().split()
b="aeiou"
count=0
for i in a:
    i=i.lower()
    if i[0] in b:
        count+=1
print(count)