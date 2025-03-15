#  Write a program to replace all the spaces in the input string with * or if no spaces found, put $ at the start and end of the string.
s = input("Enter a string: ")
if " " in s:
    s = s.replace(" ", "*")
else:
    s = "$" + s + "$"
print("Modified string:", s)
