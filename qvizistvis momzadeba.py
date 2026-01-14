for num in range(2, 1001):
    is_prime = True
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
print("1,1")
x = abs(int(input("Enter a number: ")))
y = x
rev = 0

while y > 0:
    rev = rev * 10 + y % 10
    y //= 10
print(rev)
