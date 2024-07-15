# Display even number from 0 - 15
n = 0
sum = 0
while n <= 15:
    if n % 2 == 1:
        sum += n
    n += 1
print(sum)