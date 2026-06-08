
#keywords in Python are reserved words that have a specific meaning and cannot be used as variable names, function names, or any other identifiers. They are an essential part of the Python language and are used to define the syntax and structure of the code.
#  Here is a list of all the keywords in Python:

import keyword

all_keywords = keyword.kwlist

print(f"There are {len(all_keywords)} keywords in this version of Python:\n")
for kw in all_keywords:
    print(f"• {kw}")
