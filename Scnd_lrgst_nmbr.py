a=10
b=23
c=1
if a>b and a>c:
     if b>c:
         print(f"{b} is Scnd lrgst")
     else:
         print(f"{c} is scnd lrgst")
elif b>c and b>a:
    if a>c:
        print(f"{a} is Scnd lrgst")
    else:
        print(f"{c} is Scnd lrgst")
else:
    if a>b:
        print(f"{a} is Scnd lrgst")
    else:
        print(f"{b} is Scnd lrgst")
              