# Small app to control the length of a password and robustness#

# Solution with a list
"""
password = input("Enter new password: ")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

uppercase = False
digit = False
for i in password:
    if i.isupper():
        uppercase = True

result.append(uppercase)

if all(result):
    print("Strong Password")
else:
    print("Weak Password")"""

# Solution with a dictionary

password = input("Enter new password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit


uppercase = False
digit = False
for i in password:
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase

print(result)
print(result.values())

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")
