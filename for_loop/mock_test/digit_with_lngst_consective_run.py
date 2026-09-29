n = int(input())
max_digit =-1
max_run = 0
current_digit = -1
current_run = 0

for i in str(n):
    dgt = int(i)
    if dgt == current_digit:
        current_run += 1
    else:
        current_digit = dgt
        current_run = 1
    if current_run > max_run:
        max_run = current_run
        max_digit = current_digit
print(f"Digit with the longest run: {max_digit}")
print(f"Length of the run: {max_run}")
