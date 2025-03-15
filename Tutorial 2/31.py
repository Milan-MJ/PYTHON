# Program to completely remove duplicate elements without keeping any copy
from collections import Counter

def remove_all_duplicates(lst):
    count = Counter(lst)
    return [item for item in lst if count[item] == 1]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = remove_all_duplicates(numbers)

print("List after completely removing duplicates:", unique_numbers)
