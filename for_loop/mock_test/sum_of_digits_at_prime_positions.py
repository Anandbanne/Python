#Take a number and find the sum of digits at prime-numbered positions.
n=input()
total_sum=0
for pos in range(1,len(n)+1):
    is_prime = True
    if pos <= 1:
        is_prime = False
    else:
        for j in range(2, pos):
            if pos % j == 0:
                is_prime = False
                break
    if is_prime:
        dgt=int(n[pos-1])
        total_sum+=dgt
print(total_sum)