# Types
name = "Baraa"
print(type(name))

age = 24
print(type(age))
print("Your Age is:" + str(age))

age = age + 5       # age becomes 29 (int)
age = str(age)      # age is now "29" (str)
print(type(age))    # will print <class 'str'>

age = age + 5       # ❌ ERROR! Cannot add int to str
