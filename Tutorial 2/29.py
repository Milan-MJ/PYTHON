# Write a program to do basic set operations
def input_set(name):
    return set(map(int, input(f"Enter elements of {name} set separated by space: ").split()))
set1 = input_set("First")
set2 = input_set("Second")
print("\nBasic Set Operations:")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")  
print(f"Difference (Set1 - Set2): {set1 - set2}") 
print(f"Difference (Set2 - Set1): {set2 - set1}")  
print(f"Symmetric Difference: {set1 ^ set2}")  
