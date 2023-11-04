# Write an algorithm that checks if a string contains another string.
# Interview question: Should it be case sensitive?
def contains_substring(input_string, substring):
    if not substring:
        return False
    if substring in input_string:
        return True
    else:
        return False


# Write a recursive function that takes in a number and returns the sum of the numbers from 0 to the number.
def recursive_sum(n):
    if n <= 0:
        return 0
    else:
        return n + recursive_sum(n - 1)


# Write a function that takes in a string and returns the string reversed.
def reverse_string(input_string):
    return input_string[::-1]


# Write a recursive function that takes in a list of strings and returns the words capitalized.
def capitalize_words(lst):
    if not lst:
        return []
    else:
        return [lst[0].capitalize()] + capitalize_words(lst[1:])


# Write a function that takes in a list of numbers and returns the product of the numbers in the list.
def product_of_numbers(lst):
    if not lst:
        return 1
    else:
        return lst[0] * product_of_numbers(lst[1:])


# Write an algorithm that prints the non-repeating integers in a list.
def print_non_repeating_integers(lst):
    counts = {}
    for num in lst:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    for num, count in counts.items():
        if count == 1:
            print(num)


if __name__ == "__main__":
    print(contains_substring("Hello, world", "Hello"))
    print(contains_substring("Hello, world", "hello"))
    print("_" * 40)
    print(recursive_sum(5))
    print("_" * 40)
    print(reverse_string("hello"))
    print("_" * 40)
    print(capitalize_words(["pandas", "monkeys", "koalas", "kangaroos"]))
    print("_" * 40)
    print(product_of_numbers([3, 4, 5]))
    print("_" * 40)
    print_non_repeating_integers([1, 5, 1, 6, 8, 5])
