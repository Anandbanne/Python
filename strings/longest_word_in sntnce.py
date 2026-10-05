a=input()
a=a.split()
longest=0
word=-1
for i in a:
    if len(i)>longest:
        longest=len(i)
        word=i
print(f"the longest word is {word} : {longest}")