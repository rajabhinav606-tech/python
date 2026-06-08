str = "I am a coder"

#string functions in python

print(str.upper()) #converts all characters in the string to uppercase
print(str.lower()) #converts all characters in the string to lowercase
print(str.find("a")) #finds the index of the first occurrence of a specified substring
print(str.capitalize()) #converts the first character of the string to uppercase and the rest to lowercase
print(str.replace("coder", "programmer")) #replaces a specified substring with another substring
print(str.split()) #splits the string into a list of substrings based on a specified delimiter (default is whitespace)
print(str.strip()) #removes any leading and trailing whitespace from the string
print(str.startswith("I")) #returns True if the string starts with a specified substring, otherwise returns False
print(str.endswith("r")) #returns True if the string ends with a specified substring, otherwise     
print(str.count("a")) #returns the number of occurrences of a specified substring in the string
