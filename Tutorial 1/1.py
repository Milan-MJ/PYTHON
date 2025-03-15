# Write a python program to input a time in seconds and print the time in HH:MM:SS format.
seconds = int(input("Enter time in seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60
print(f"{hours:02}:{minutes:02}:{remaining_seconds:02}")
