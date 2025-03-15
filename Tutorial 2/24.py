#  Finding the mode of list of numbers(A number that appears most often is the mode.)
from collections import Counter
nums = list(map(int, input("Enter numbers: ").split()))
counts = Counter(nums)
mode = max(counts, key=counts.get)
print("Mode:", mode)
