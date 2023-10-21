# arb_args - Takes in any number of arguments and prints them one at a time.
def arb_args(*args):
    for arg in args:
        print(arg)


# inner_func - Takes in two integers. 
# Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.
def inner_func(num1, num2):
    def add_nums(num1, num2):
        return num1 + num2

    def multiply_nums(num1, num2):
        return num1 * num2

    result = add_nums(num1, num2) + multiply_nums(num1, num2)
    print(result)


# lunch_lady - Takes in two strings: a student's name and their lunch preference. 
# The function should print both strings. 
# If a lunch preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady(name, preference="Mystery Meat"):
    print(name, preference)


# sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(num1, num2):
    return num1 + num2, num1 * num2


# alias_arb_args - Should be arb_args but assigned an alias. 
# Remember, variables can hold functions in Python just like they can in JS. 
# Alternatively, you can call a function from inside another function.
alias_arb_args = arb_args


# arb_mean - Accepts any number of integers and prints their average.
def arb_mean(*args):
    if len(args) == 0:
        print("No arguments provided")
    else:
        print(sum(args) / len(args))


# arb_longest_string - Accepts any number of strings and returns the longest one.
def arb_longest_string(*args):
    if len(args) == 0:
        return None
    else:
        return max(args, key=len)


arb_args(1, 2, 3, 4, 5)
print("_"*40)
inner_func(5, 10)
print("_"*40)
lunch_lady("Bob", "Pizza")
lunch_lady("Andrew")
print("_"*40)
print(sum_n_product(5, 10))
print("_"*40)
alias_arb_args(1, 2, 3, 4, 5)
print("_"*40)
arb_mean(1, 2, 3, 4, 5)
arb_mean()
print("_"*40)
print(arb_longest_string("a", "ab", "abc", "abcd"))