
print(35)
print(98+69)

# Find largest number from user input (enter numbers separated by space)
nums = list(map(float, input("Enter numbers separated by space: ").split()))
if nums:
    print("Largest number is:", max(nums))
else:
    print("No numbers entered")