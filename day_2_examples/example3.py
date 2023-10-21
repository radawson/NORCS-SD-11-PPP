def print_all(*args):
    print("_" * 40)
    for arg in args:
        print(arg)

print_all(1, "x", 3.2126, "buffalo")

print_all(12)

print_all ("a", "b","c")