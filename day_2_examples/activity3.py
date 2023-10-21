def name_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def all_true(iterable):
    return all(iterable)

def one_true(iterable):
    return any(iterable)

def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

def recursive_deduplicate(s):
    if len(s) == 0:
        return s
    elif len(s) == 1:
        return s
    elif s[0] == s[1]:
        return recursive_deduplicate(s[1:])
    else:
        return s[0] + recursive_deduplicate(s[1:])

def recursive_reverse(s):
    if len(s) == 0:
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]

if __name__ == "__main__":
    name_args(name="John", age=30, country="USA")
    print(all_true([True, True, True]))
    print(one_true([False, False, True]))
    print(recursive_factorial(5))
    print(recursive_deduplicate("aaabbbccc"))
    print(recursive_reverse("Hello World!"))