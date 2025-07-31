# ✅ Comparison Operators in Python
print(10 == 10)   # True — equal to
print(10 != 10)   # False — not equal to
print(7 > 3)      # True — greater than
print(7 >= 3)     # True — greater than or equal to
print(3 < 7)      # True — less than
print(7 <= 7)     # True — less than or equal to


# Case-sensitive comparison
print("a" == "A")  # False — lowercase is NOT equal to uppercase
# Case-insensitive comparison
print("a".lower() == "A".lower())  # True


# Alphabetical comparison using strings
print("a" < "b")  # True — because "a" comes before "b" in ASCII order


# WRONG: This will cause a syntax error!
# print("a" = "A")  # You cannot use = inside a comparison like this.

#  CORRECT:
print("a" == "A")  # False, because string comparison is case-sensitive

# Assignment example:
x = "a"            # This assigns the value "a" to variable x
print(x == "a")    # True



# Is age between 18 and 30?
age = 18
print(18 <= age <= 30)  # True


# Is age between 18 and 30?
age = 35
print(18 <= age <= 30)  # False


