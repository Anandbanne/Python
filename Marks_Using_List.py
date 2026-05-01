names=["Anandu","Sai","Rohith","Deekshith","Somi"]
marks=[87,35,67,90,31]
p=1
for i in range(5):
    if marks[i]>35:
        print(f"{p+1} {names[i]} has scored {marks[i]}%")
        p=p+1
        