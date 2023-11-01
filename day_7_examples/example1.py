values = [1, 2, 3, 4, 5, 6]


def function1(values):
    for value in values:
        print(value)


def function3(values):
    for x in values:
        for y in values:
            print(x, y)


def function3b(values):
    for x in values:
        print(x)
    for y in values:
        print(y)


def function4(values):
    for i in range(4):
        print("Python is great")

    print("Software Engineering is awesome!")
    print("Software Engineering is awesome!")

    for value in values:
        print(value)

    for value in values:
        print(value)


def function5(n):
    test_list = []

    for num in range(n):
        test_list.append(f"{num}add me")

    return test_list

if __name__ == "__main__":
    # function1(values)
    # function3(values)
    #function4(values)
    
    print(function5(12))
