print(True)         # ➜ True
print(False)        # ➜ False
print(type(True))   # ➜ <class 'bool'>


print(bool(123))     # ➜ True     (non-zero number)
print(bool("Hi"))    # ➜ True     (non-empty string)

print(bool(()))      # ➜ False    (empty tuple)
print(bool(0))       # ➜ False    (zero)
print(bool(""))      # ➜ False    (empty string)
print(bool(None))    # ➜ False    (None is always False)



email = ""
phone = "017-1234"
username = "baraa123"

# Allows registration if any field is filled
# (at least one non-empty value → True)
print(any([email, phone, username]))  # ➜ True

#  Allows registration only if all fields are filled
#  (every value must be non-empty → True)
print(all([email, phone, username]))  # ➜ False



# Check if values are of a certain type
print(isinstance(123, int))     # ➜ True
print(isinstance(True, str))    # ➜ False

# Check how strings start or end
print("Hello".endswith("o"))    # ➜ False
print("Hello".startswith("o"))  # ➜ False
