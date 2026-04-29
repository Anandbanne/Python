import time
print("\033[1;33]")
for  i in range(1,11):
    time.sleep(3)
    for j in range(1,11):
        print(f"{i*j:02d} ",end=" ")
    print()    