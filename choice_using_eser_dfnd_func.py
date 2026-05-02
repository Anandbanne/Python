def sq():
    s=int(input("Enter the number:"))
    print(f"Area: {s*s}")
def cir(r):
    print(r*r*3.14)
def rect(a,b):
    print(a*b)    _


while True:
    print("1.Square")
    print("2.Circle")
    print("3.Rectangle")
    print("4.Exit")
    ch=int(input("Enter the choice:"))
    if ch==1:
        sq()
    elif ch==2:
        cir(3)
    elif ch==3:
        rect(4,3)
    else:
        break