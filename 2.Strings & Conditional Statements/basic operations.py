
#concatenation is the operation of joining two or more strings together. In Python, you can concatenate strings using the + operator. Here is an example:
str1 = "Hello"
str2 = "World"
str3 = str1 + " " + str2
print(str3) 

#length of string is the number of characters in a string, including spaces and punctuation. In Python, you can find the length of a string using the len() function. Here is an example:
str1 = "Hello World,This is a Length of String."
print(len(str1))   

#string indexing is the process of accessing individual characters in a string using their position. In Python, you can access characters in a string using square brackets [] and the index of the character. The index starts at 0 for the first character, 1 for the second character, and so on. Here is an example:
str1 = "Hello_World"
print(str1[0])  # Output: H
print(str1[6])  # Output: W
print(str1[4]) # Output: o

#string slicing is the process of extracting a portion of a string using a range of indices. In Python, you can slice a string using square brackets [] and the start and end indices separated by a colon :. The start index is inclusive, while the end index is exclusive. Here is an example:
str1 = "Hello World"  #ending index is not included in the output
print(str1[0:5])  # Output: Hello
print(str1[6:11]) # Output: World
print(str1[:5]) #[0:5] can be written as [:5] which means start from the beginning of the string and go up to index 5 (exclusive)
print(str1[6:]) #[6:11] can be written as [6:] which means start from index 6 and go to the end of the string

#negative indexing is a way to access characters in a string from the end of the string instead of the beginning. In Python, you can use negative indices to access characters in a string. The index -1 refers to the last character, -2 refers to the second last character, and so on. Here is an example:
str1 = "Hello World"
print(str1[-1])  # Output: d
print(str1[-6])  # Output: W    
print(str1[-5])  # Output: o



