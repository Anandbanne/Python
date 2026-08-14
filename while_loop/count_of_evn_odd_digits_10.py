n=int(input())
even=0
odd=0
while n>0:
    a=n%10
    if a%2==0:
        even+=1
    else:
        odd+=1
    n//=10
print(f"even digits {even}")
print(f"odd digits {odd}")    
        