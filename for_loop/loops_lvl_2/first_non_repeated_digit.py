n=int(input())
freq=[0]*10
for i in str(n):
    dgt=int(i)
    freq[dgt]+=1
print(freq)
Found =False
for i in str(n):
    d=int(i)
    if freq[d]==1:
        print(f"{d} is the first non repeat digit.")
        Found=True
        break
if not Found:
    print("no non repeat digit.")