a=int(input())
b=int(input())
l_p=-1
s_p=-1
for i in range(a,b+1):
     if i<=1:
         continue
     is_prime=True
     for j in range(2,i):
         if i%j==0:
             is_prime=False
             break
     if is_prime:
         if i>l_p:
             s_p=l_p
             l_p=i
         elif i<l_p and i>s_p:
             s_p=i
print(s_p)
