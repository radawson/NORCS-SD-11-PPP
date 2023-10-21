#A function named hello() that prints a greeting to the user. 
#This function should accept no arguments and returns nothing.
def hello():
    print("Hello, User!")

#A function named pack() that accepts three arguments, 
#and returns a single list with the three arguments inside as list elements.
def pack(a, b, c):
    return [a, b, c]

#A function called eat_lunch(). 
# This function should accept a list of any length, 
# and print out a series of strings that say "First I eat __" 
# (the first element of the list), 
# and "Next I eat ___" (for the following elements in the list). 
# If the list is empty, print "My lunchbox is empty!". 
# The function should not return anything.
def eat_lunch(lunchbox):
    if len(lunchbox) == 0:
        print("My lunchbox is empty!")
    else:
        print("First I eat " + lunchbox[0])
        for i in range(1, len(lunchbox)):
            print("Next I eat " + lunchbox[i])
        print("I'm full!")

hello()
print(pack(1, 2, 3))
print(pack("apple", "banana", "carrot"))
eat_lunch(["apple", "banana", "carrot", "doughnut"])
eat_lunch([])
