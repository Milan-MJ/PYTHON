# Write a program to remove characters at odd index positions from a string.
s = input("Enter a string: ")
result = "".join(s[i] for i in range(len(s)) if i % 2 == 0)
print("Modified string:", result)
