unsorted_list =  [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_list = sorted(unsorted_list,key=lambda x:x[1])

#unsorted_list.sort(key=lambda x:x[1])
print(unsorted_list)
print(sorted_list)
