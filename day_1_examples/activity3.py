#A function that accepts no arguments and is named say_hello and returns nothing; 
#it just prints hello.
def say_hello():
    print("Hello")


#A sum function that accepts two integers and returns the sum.
def sum(a, b):
    return a + b

#An average function that accepts two numbers and returns the average.
def average(a, b):
    return (a + b) / 2

#A function that accepts a first name and a last name and 
# formats them to "{last_name}, {first_name}" (returns a string).
def format_name(first_name, last_name):
    return last_name + ", " + first_name

#A function that accepts a first name, last name, graduation year, 
# and student number and returns those four items together in a list.
def student_info(first_name, last_name, graduation_year, student_number):
    return [first_name, last_name, graduation_year, student_number]

#A function that accepts an integer and returns whether it is above 18 or not (Boolean).
def is_over_18(age):
    return age > 18

#A function that takes a string and prints the string in reverse (no return value).
def reverse_string(string):
    print(string[::-1])

say_hello()
print(sum(1, 2))
print(average(1, 2))
print(format_name("Luke", "Skywalker"))
print(student_info("Luke", "Skywalker", 2020, 123456))
print(is_over_18(20))
print(is_over_18(15))
reverse_string("Hello, World!")