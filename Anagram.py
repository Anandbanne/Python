a=input("Enter the String: ")
b=input("String: ")
a2="".join(i.lower() for i in a if i.isalnum())
b2="".join(i.lower() for i in b if i.isalnum())
a1=sorted(a2)
b1=sorted(b2)
if a1==b1:
    print("Anagram")
else:
    print("No")
    