# Remove duplicate elements from a list.
def remove_duplicates(lst):
    return list(set(lst))
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_numbers = remove_duplicates(numbers)
print("List after removing duplicates:", unique_numbers)
