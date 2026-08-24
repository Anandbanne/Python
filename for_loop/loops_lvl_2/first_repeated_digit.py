n=int(input())
freq=[False]*10
Found=False
for i in str(n):
    dgt=int(i)
    if freq[dgt]:
        print(f"first repeated digit is {dgt}")
        Found=True
        break
    freq[dgt]=True
if not Found:
    print("NO repeated digit.")