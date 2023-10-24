unsorted_list =  [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_list = sorted(unsorted_list,key=lambda x:x[1])

#unsorted_list.sort(key=lambda x:x[1])

original_list = [3, 6, 9, 2]
cubed_list = list(map(lambda x: x**3, original_list))
cubed_list2 = [x**3 for x in original_list]

is_even = lambda x: x % 2 ==0
even_list = [is_even(x) for x in original_list]

list1 = [i for i in range(1,101)]
 
sentence = "The quick brown fox jumped over the fence."
word_list = sentence.split()
word_lengths = {word: len(word) for word in word_list}

if __name__ == "__main__":
    print(unsorted_list)
    print(sorted_list)

    print(cubed_list)
    print(cubed_list2)

    print(even_list)

    print(list1)

    print(word_lengths)