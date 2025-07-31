# Data Types
a = 10        # int
b = 3.15      # float
c = "Hello"   # str
d = 'Hi'      # str
e = "1234"    # str (looks like a number, but it's a string)
f = True      # bool
g = False     # bool
h = None      # NoneType
i = ""        # str - blank (empty string)
j = " "       # str - contains one empty space


text = "hi"
number = 10

print(type(text))
print(type(number))


text = "hi"
number = 10

print(text.upper())           # Converts text to uppercase -> "HI"
print(number.bit_length())    # Returns number of bits to represent 10 -> 4
print(text.bit_length())      # ❌ Error! Strings don't have bit_length()


Create 5 variables – each with a different data type:
- Your age
- Your height (with decimals)
- Your name
- Are you a student?
- Something with no value yet
