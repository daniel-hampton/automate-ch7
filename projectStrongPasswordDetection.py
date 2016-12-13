# This code is for the Strong Password Protection practice project at the end of Chapter 7 in Automate the Boring Stuff

import re

# Asks the user for password to test.
userInputString = input('Please enter the password to be test: ')

'''
Password requirements:
    1. At least eight characters long
    2. Contains both uppercase and lowercase characters
    3. Contains at least one digit
'''
# Define regex for uppercase, lowercase, and one or more digits.
upperCaseRegex = re.compile(r'[A-Z]+')
lowerCaseRegex = re.compile(r'[a-z]+')
digitRegex = re.compile(r'\d+')

# Checks to see if password is 8 characters or more.
if len(userInputString) >= 8:
    print('PASS: Your password is long enough.')
else:
    print('FAIL: Your password is too short')

# Checks for uppercase.
mo = upperCaseRegex.search(userInputString)
if mo is None:
    print('FAIL: Your password needs an uppercase character')
else:
    print('PASS: Your password contains at least one uppercase character')

# Checks for lowercase
mo = lowerCaseRegex.search(userInputString)
if mo is None:
    print('FAIL: Your password needs an lowercase character')
else:
    print('PASS: Your password contains at least one lowercase character')

# Checks for digits
mo = digitRegex.search(userInputString)
if mo is None:
    print('FAIL: Your password needs a numerical digit')
else:
    print('PASS: Your password contains at least one numerical digit')
