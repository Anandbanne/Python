a=input()
b="aeiouAEIOU"
vowels=0
consonants=0
for i in a:
    if i.isalpha():
        if i in b:
            vowels+=1
        else:
            consonants+=1
print(vowels)
print(consonants)