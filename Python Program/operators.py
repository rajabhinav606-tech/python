#arthematics operators 

a = 4
b = 3

# sum = a+b correct way but we use here another way
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division in python division always results in float 
print(a//b) #floor division Floor division in Python is a mathematical operation performed using the double forward slash operator (//) that divides two numbers and rounds the result down to the nearest whole number (towards negative infinity). It provides the quotient as an integer, discarding any fractional part.
print(a%b) #modulus operator gives the remainder after division
print(a**b) #exponentiation operator gives the result of a raised to the power of b  here 4 raised to the power of 3 is 4*4*4 = 64


#Relational operators
print(a>b) #greater than operator
print(a<b) #less than operator
print(a>=b) #greater than or equal to operator
print(a<=b) #less than or equal to operator
print(a==b) #equality operator checks if a and b are equal or not
print(a!=b) #not equal to operator checks if a and b are not equal or not

#assignment operators
num = 10 #assignment operator assigns the value 10 to variable num
num += 5 #num = num + 5 adds 5 to the current value of num and assigns the result back to num
print(num) #prints the updated value of num which is 15
num -= 3 #num = num - 3 subtracts 3 from the current value of num and assigns the result back to num
print(num) #prints the updated value of num which is 12
num *= 2 #num = num * 2 multiplies the current value (12) of num by 2 and assigns the result back to num
print(num) #prints the updated value of num which is 24
num /= 4 #num = num / 4 divides the current value (24) of num by 4 and assigns the result back to num
print(num) #prints the updated value of num which is 6.0
num %= 4 #num = num % 4 calculates the remainder of  current num value (6) divided by 4 and assigns the result back to num
print(num) #prints the updated value of num which is 2.0
num **= 3 #num = num ** 3 raises the current value (2) of num to the power of 3 and assigns the result back to num
print(num) #prints the updated value of num which is 8.0


#logical operators
print(not False)
print(not True)

print(a>2 and b<5) #logical and operator returns True if both conditions are true
print(a>5 or b<5) #logical or operator returns True if at least one of the conditions is true