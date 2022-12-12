name_sentence = input("Enter a list of first names seperated by spaces: ")
name_list = name_sentence.split()
single_sentence = ''.join(name_list)
print("Number of occurrences of the letter `a` is:", single_sentence.count('a'))
