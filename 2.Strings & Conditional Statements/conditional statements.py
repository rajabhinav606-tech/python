
"""if-elif-else statements are used in Python to make decisions based on
certain conditions. They allow you to execute different blocks of code
depending on whether a condition is true or false.

Example:
"""
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are exactly 18 years old.")
else:
    print("You are an adult.")
