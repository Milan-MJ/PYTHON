#  Consider a list consisting of integers, floating point numbers and strings.Separate them into different lists depending on the data
data = input("Enter elements: ").split()
integers = [int(x) for x in data if x.isdigit()]
floats = [float(x) for x in data if "." in x]
strings = [x for x in data if not x.replace(".", "").isdigit()]
print("Integers:", integers, "\nFloats:", floats, "\nStrings:", strings)
