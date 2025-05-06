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

# Find the greatest among three numbers

a = 10
b = 25
c = 15

if a >= b and a >= c:
    print("The greatest number is ")
    print(a)
elif b >= a and b >= c:
    print("The greatest number is ")
    print(b)
else:
    print("The greatest number is ")
    print(c)

# Prime Number Check
print('\nPrime Number Check:')
n = 29  # You can change this value to test other numbers

# Check for prime
if n <= 1:
    print(n)
    print("is a Prime Number")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(n)
            print("is a NOT Prime Number")
            break
    else:
         print(n)
         print("is a Prime Number")
