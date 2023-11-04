def contains_substring(input_string, substring):
    if not substring:
        return False
    if substring in input_string:
        return True
    else:
        return False

def recursive_sum(n):
    if n <= 0:
        return 0
    else:
        return n + recursive_sum(n - 1)

def reverse_string(input_string):
    return input_string[::-1]
    
def capitalize_words(lst):
    if not lst:
        return []
    else:
        return [lst[0].capitalize()] + capitalize_words(lst[1:])


def product_of_numbers(lst):
    if not lst:
        return 1
    else:
        return lst[0] * product_of_numbers(lst[1:])

if __name__ == "__main__":
    print(contains_substring("Hello, world", "Hello"))
    print(contains_substring("Hello, world", "hello"))