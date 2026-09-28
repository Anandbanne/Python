 text = input()

vowels = 0
consonants = 0
vowel_chars = "aeiouAEIOU"

for char in text:
    if char.isalpha():
        if char in vowel_chars:
            vowels += 1
        else:
            consonants += 1

print(f"Vowels = {vowels}")
print(f"Consonants = {consonants}")
