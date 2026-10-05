a=input()
a=a.split()
shortest=float("inf")
word=-1
for i in a:
    if len(i)<shortest:
        shortest=len(i)
        word=i
print(f"the shortest word is ' {word} ' : {shortest}")