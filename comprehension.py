nums = input("Numbers: ").split()
nums = list(map(int, nums))
pos_nums = [x for x in nums if x >= 0]
square_nums = [x*x for x in nums]

print("Positive numbers are:", pos_nums)
print("Square of the numbers are:", square_nums)

vowels = 'aeiouAEIOU'

sentence = input("Enter a string: ")
sentence_vowels = ', '.join([x for x in sentence if x in vowels])
print("Vowels in sentence are:", sentence_vowels)

word = input("Enter a word: ")
word_ord = [ord(x) for x in word]
print("ord values of letters are", word_ord)
