sentence = input("Enter a sentence: ")
words = sentence.split()

word_dict = {}

for x in words:
    if x not in word_dict.keys():
        word_dict[x] = 1
    else:
        word_dict[x] += 1

print(word_dict)
