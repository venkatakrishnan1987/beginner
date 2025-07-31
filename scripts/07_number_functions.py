x = 5
y = 5.7
z = 2 + 3j

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>


x = "24"
print(type(x))    # <class 'str'>

x = int(x)
print(type(x))    # <class 'int'>

print(x * 3)      # 72


x = 3.14
print(int(x))


x = 3
print(float(x))


x = 3      # real part
y = 4      # imaginary part
print(complex(x, y))


print(2 + 3)     # ➜ 5 (Addition)
print(5 - 3)     # ➜ 2 (Subtraction)
print(4 * 2)     # ➜ 8 (Multiplication)
print(7 / 2)     # ➜ 3.5 (True division → returns float)
print(7 // 2)    # ➜ 3 (Floor division → drops the decimal)
print(9 % 2)     # ➜ 1 (Modulus → remainder)
print(2 ** 3)    # ➜ 8 (Exponentiation → 2 to the power of 3)


x = 2         # Step 1: Initialize x with value 2

x += 3        # Step 2: x = x + 3 → x becomes 5
print(x)      # ➜ 5

x -= 1        # Step 3: x = x - 1 → x becomes 4
print(x)      # ➜ 4

x *= 2        # Step 4: x = x * 2 → x becomes 8
print(x)      # ➜ 8


print(abs(2 - 10))




import math

# Rounding Numbers
price = 35.54879865

# Built-in round(): round to nearest whole number
print(round(price))          # ➜ 36

# Round to 2 decimal places
print(round(price, 2))       # ➜ 35.55

# Round to 1 decimal place
print(round(price, 1))       # ➜ 35.5

# Round down to nearest whole number
print(math.floor(price))     # ➜ 35

# Round up to nearest whole number
print(math.ceil(price))      # ➜ 36

# Truncate the decimal part (drop it without rounding)
print(math.trunc(price))     # ➜ 35

# Convert to int (same as truncation)
print(int(price))            # ➜ 35



import random

# Generate a random float between 0 and 1 (uncomment to try)
print(random.random())  # ➜ 0.7321 (example)

# Simulate a dice roll: random integer between 1 and 6 (inclusive)
print(random.randint(1, 6))  # ➜ 4 (varies every time)



x = 7.0
print(x.is_integer())  # ➜ True → 7.0 is a float, but it represents an integer

y = 7.1
print(y.is_integer())  # ➜ False → 7.1 is not a whole number



x = 70.4

print(isinstance(x, int))    # ➜ False → x is not an integer
print(isinstance(x, float))  # ➜ True → x is a float




🚀 Python Challenge
Generate a random integer between 1 and 100, and check if the result is an even number.
