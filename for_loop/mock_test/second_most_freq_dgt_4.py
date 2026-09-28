n = int(input())

freq = [0] * 10

for ch in str(n):
    digit = int(ch)
    freq[digit] += 1

largest_freq = -1
second_freq = -1
largest_digit = -1
second_digit = -1

for digit in range(10):
    if freq[digit] == 0:
        continue

    if freq[digit] > largest_freq:
        second_freq = largest_freq
        second_digit = largest_digit

        largest_freq = freq[digit]
        largest_digit = digit

    elif freq[digit] < largest_freq and freq[digit] > second_freq:
        second_freq = freq[digit]
        second_digit = digit

print(second_digit)
