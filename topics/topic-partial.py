# 1. Basic Example
# Fixing one argument of a function:

from functools import partial


def multiple(x,y):
    return x*y

#normal call
# multiple(2,2)

double = partial(multiple,2)
print(double(5)) # output 10

# Here, double() is equivalent to calling multiply(2, y), making it more convenient.

# 2. Using Named Arguments

# You can also use keyword arguments (kwargs):

def greet(name,greeting="Hello"):
    return f"{greeting}, {name}!"

say_hi = partial(greet,greeting="Hello")
print(say_hi("Sky"))
# The greeting argument is pre-set to "Hi", but name remains flexible.

# 3. Using partial() in Functions That Accept Variable Arguments (*args, **kwargs)

def show_info(name, age, city):
    return f"{name}, {age}, {city}"

person_info = partial(show_info, city="NY")
print(person_info("Sky", 25))

# The function still requires name and age, but city is always "New York".


# 4. Using partial() with Built-in Functions

# partial() is useful for adapting built-in functions like map(), filter(), and sorted().

# map, filter
str_nums = ["10", "20", "30", "40"]

# # without partial

print("without partial")
print(list(map(int,str_nums)))

# # with partial
print("with partial")
to_int = partial(map, int)
print(list(to_int(str_nums)))


# # without partial
str_nums = "10,20,30,40"
print(list(map(int, str_nums.split(","))))

# # with partial
str_nums = "10,20,30,40"
split_and_int = partial(map, int, str_nums.split(","))
print(list(split_and_int()))


# 5. Using partial() in Class Methods

class Calculator:
    def operation(self, x, y, op):
        if op == "add":
            return x + y
        elif op == "multiply":
            return x * y
        return None

calc = Calculator()

# Create specialized functions
add = partial(calc.operation, op="add")
multiply = partial(calc.operation, op="multiply")

print(add(4, 5))       # Output: 9
print(multiply(4, 5))  # Output: 20


# 6. Comparison with Lambda Functions
# partial() is often an alternative to lambda, but it improves readability:

# Using lambda
# square = lambda x: power(x, 2)

# # Using partial (more readable)
# square = partial(power, exponent=2)

# While lambda works well for simple cases, partial() is more explicit and useful when working with existing functions.



# 7. Automating Email Sending with Callbacks
# In automated systems, partial() helps pass user details dynamically.

from functools import partial

def send_email(user, subject, body):
    print(f"Sending email to {user} with subject: {subject}")
    print(f"Body: {body}\n")

users = ["alice@example.com", "bob@example.com", "charlie@example.com"]

# Creating specialized email functions for each user
for user in users:
    email_sender = partial(send_email, user, "Welcome!", "Hello, thanks for joining us!")
    email_sender()  # Calls send_email(user, "Welcome!", "Hello, thanks for joining us!")

# How it Works?
# partial(send_email, user, "Welcome!", "Hello!") pre-fills user and message details.
# The email function can be used in job schedulers or cron jobs.