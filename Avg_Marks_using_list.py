names=["ANand","Rohith","Deekshith","Sai","Akash","lucky"]
marks=[[70,80,98],[12,34,78],[78,38,67],[98,76,67],[88,78,65]]
for i in range(5):
    a=sum(marks[i])//3
    print(f"{i+1}. {names[i]} has scored {a}")