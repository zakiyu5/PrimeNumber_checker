print("lets start to see if prime or not prime ")
num = int(input("enter the number to check : "))
if num <= 1:
    print("The number is not prime.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime == True
            break
    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")

print("prime numbers between -50 to 50 ")
for i in range(-50, 51):
    if i <= 1:
        continue
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, "is prime")