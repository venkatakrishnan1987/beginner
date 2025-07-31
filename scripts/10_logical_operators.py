
# Logical Operations

print(3 > 1 and 5 < 1)   # False: First is True, second is False
print(3 > 1 and 5 > 1)   # True: Both are True

print(3 > 1 or 5 < 1)    # True: First is True, second is False
print(3 > 1 or 5 > 1)    # True: Both are True




# Checks if the system is under pressure
cpu_usage = 70
memory_usage = 90

print(cpu_usage > 90 or memory_usage > 90)  # False: both values are not above 90



# Checking user credentials before login
email = True
password = False

print(email and password)  # False: both conditions must be True to pass



# Using 'not' to reverse boolean values and check for falsy values

print(not 3 > 2)       # False: 3 > 2 is True, not True becomes False
print(not True)        # False
print(not False)       # True
print(not not False)   # False: not False is True, not True is False

name = ""
print(not name)        # True: empty string is falsy, not falsy is True
print(not 10)          # False: 10 is truthy, not True is False



# Allow access only if the user is logged in
# or they are a guest
# but they must not be banned

is_logged_in = True
is_guest = False
is_banned = True

# Using parentheses to group access logic correctly
print(is_logged_in or is_guest and not is_banned)
print((is_logged_in or is_guest) and not is_banned)



Python Challenges
1. Check if a user's name is not empty and the age is greater than or equal to 18
2. Check if the password is at least 8 characters long and does not contain spaces
3. Check if a user’s email is not empty, contains '@', and ends with '.com'
4. Check if a username is a string, is not None, and is longer than 5 characters
5. Check if the user is either an admin or a moderator, and either they’re not banned or they’ve verified their email



# IS IN
print("f" not in "python")
print(3 not in [1, 2, 3])

# Security check: ensure the domain is not banned
domain = "spam.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)


x = ['a', 'b', 'c']
y = ['a', 'b', 'c']

print(x == y)  # True: same content
print(x is y)  # False: different objects

x = 10
y = 10

print(x == y)  # True: same value
print(x is y)  # True: same object (small integers are interned in Python)


x = ['a', 'b', 'c']
y = x

print(x == y)  # True: values are the same
print(x is y)  # True: both variables point to the same object in memory


# Make sure the email exists, and it’s not empty.

email = "b@gmail.com"
print(email != "")

email = None
print(email is not None and email != "")




