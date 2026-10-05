a=input()
b="aeiou"
count=0
a=a.lower()
for i in a:
    if i in b:
        count+=1
print(f"the number of vowels are {count}")