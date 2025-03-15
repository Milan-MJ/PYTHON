# Program to read a string and remove the given words from the string.
s = input("Enter string: ")
words = input("Enter words to remove (space-separated): ").split()
for word in words:
    s = s.replace(word, "")
print("Modified string:", s)