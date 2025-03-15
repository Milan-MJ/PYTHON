# The Password should satisfy the following criteria:
#  1. Contains at least one letter between a and z
#  2. Contains at least one number between 0 and 9
#  3. Contains at least one letter between A and Z
#  4. Contains at least one special character from $, #, @
#  Minimum length of password: 6
import re
password = input("Enter password: ")
if (len(password) >= 6 and re.search("[a-z]", password) and
    re.search("[A-Z]", password) and re.search("[0-9]", password) and
    re.search("[$#@]", password)):
    print("Valid Password")
else:
    print("Invalid Password")
