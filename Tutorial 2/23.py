# Program to read list of numbers and find the median
nums = sorted(map(int, input("Enter numbers: ").split()))
mid = len(nums) // 2
print("Median:", (nums[mid] if len(nums) % 2 else (nums[mid-1] + nums[mid]) / 2))
