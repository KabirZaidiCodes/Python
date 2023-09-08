# if-else conditional statements in Python

a = int(input("Enter your age:"))
print("Your age is:", a)

if(a>18):
    print("You can drive")
else:
    print("You cannot drive")

# The above code is an example of an if else conditional statement

# Conditional Operators ->
# <, >, =, ==, <= and >=

# elif statements in Python
num = 0
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")

# The above code is an example of an elif conditional statement

# Nested if statements in Python
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

# The above code is an example of a Nested if conditional statement
