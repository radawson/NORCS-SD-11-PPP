def split_name(fullname):
    first, last = fullname.split()
    return first,last

name1 = split_name("Robert Johnson")
print(name1)

name2 = split_name("Benjamin Franklin")
print(name1)
print(name2)