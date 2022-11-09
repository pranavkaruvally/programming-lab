sentence = input("Enter a sentence:")
first_letter = sentence[0].lower()

substituted_second_half = ['$' if (x.lower() == first_letter) else x for x in sentence[1:]]
final_sentence = first_letter + ''.join(substituted_second_half)

print(final_sentence)
