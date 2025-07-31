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


# Math
password = "123a58478as"
print(len(password))

if len(password) < 8:
    print("Your Password is too short!")


# Math
text = """
Python is easy to learn.
Python is powerful$.
Many people love python.
"""

print(text.count("Python"))
print(text.count("python"))
print(text.count("$"))

# Transformations

# Transformations
price = "1234,56"
print(price.replace(",", "."))

phone = "176-1234-56"
print(phone.replace("-", "/"))
print(phone.replace("-", ""))

Convert the messy phone number into a clean number format with only digits
"+49 (176) 123-4567"
00491761234567



# Transformations
first_name = "Michael"
last_name = "Scott"
last_name = first_name + "-" + last_name
print(last_name)

# Transformations
folder = "C:/Users/Baraa/"
file = "report.csv"
full_file_path = folder + file
print(full_file_path)


name = "Sam"
age = 34
is_student = False

# Method 1: Using string concatenation + str()
print("My name is " + name + ", I am " + str(age) + " years old, and student status is " + str(is_student) + ".")

# Method 2: Using an f-string (cleaner and recommended)
print(f"My name is {name}, I am {age} years old, and student status is {is_student}.")

print(f"2 + 3 = {2 + 3}")        # Evaluates the expression: Output → 2 + 3 = 5
print(f"{{This is me}}")         # Prints literal curly braces: Output → {This is me}

# Transformations
stamp = "2026-09-20 14:30"
print(stamp.split(" "))

# Transformations
csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(", "))

# Transformations
print("ha" * 3)
print("======================")

print("=" * 30)


# Indexes & Slicing
text = "Python"

# Extract the first character
print(text[0])     # P
print(text[-6])    # P

# Extract the last character
print(text[5])     # n
print(text[-1])    # n

# Extract 'h'
print(text[3])     # h

# Indexes & Slicing
date = "2026-09-20"

# Extract the Year
print(date[0:4])   # 2026
print(date[:4])    # 2026

# Extract the Month
print(date[5:7])   # 09

# Extract the Day
print(date[8:])    # 20
print(date[-2:])   # 20


# Whitespace Cleanup
text = " Engineering".lstrip()
print(text)

text = "Engineering ".rstrip()
print(text)

text = "  Engineering ".strip()
print(text)

text = "Data Engineering".strip()
print(text)

text = "###Abc###".strip("#")
print(text)

# Case Conversions
text = "python PROGRAMMING"
print(text.lower())   # Converts all to lowercase
print(text.upper())   # Converts all to uppercase

# Case Conversions
search = "Email ".lower().strip()
data = " emAil".lower().strip()

print(search == data)


Turn the messy string into a single clean summary with name, role, and age
"968-Maria, ( D@ta Engineer );; 27y"
Clean the string!
name: maria | role: data engineer | age: 27

# Search
phone = "+48-176-12345"
print(phone.startswith("+49"))

email = "baraa@outlook.com"
print(email.endswith("gmail.com"))

file = "data_backup.csv"
print(file.endswith(".csv"))

# Search
phone = "+48-176-12345"
print(phone.startswith("+49"))          # False

email = "baraa@outlook.com"
print(email.endswith("gmail.com"))      # False

print("@" in email)                     # True

url = "https://api.company.com/v1/data"
print("/api" in url)                    # True


# Search
phone1 = "+48-176-12345"
phone2 = "48-654-16548"
phone3 = "0048-654-16548"

print(phone1[phone1.find("-") + 1:])  # 176-12345
print(phone2[phone2.find("-") + 1:])  # 654-16548
print(phone3[phone3.find("-") + 1:])  # 654-16548

print(phone1.find("-"))              # 3





