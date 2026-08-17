n = int(input("Enter number: "))
is_prime = True
if n <= 1:
    is_prime = False
else:
    i = 2
    while i < n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
if is_prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
