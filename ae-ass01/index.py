print('Content-Type: text/plain')
print('Hello World')


# Factorial
print('\nFactorial of 5 is:-')
ans = 1
for i in range(1, 6):
    ans *= i
print(ans)

# Fibonacci Series
num1 = 0
num2 = 1
a = 0

print('\nFibonacci Series :-')
print('0')
print('1')
for i in range(1, 6):
    a = num1 + num2
    num1 = num2
    num2 = a
    print(a)

# Print Name, Seat Number, Department
print('\nRepeated Info:\n')
for i in range(1, 5):
    print("Anish")
    print("123")
    print("IT\n")

# Table of 5
print('\nTable of 5:\n')
for i in range(1, 11):
    print("5 x {} = {}".format(i, 5 * i))


# Prime Number Check
print('\nPrime Number Check:')
n = 29  # You can change this number to test others
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{n} is a Prime Number")
else:
    print(f"{n} is not a Prime Number")