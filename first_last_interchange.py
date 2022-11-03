sentence = input("Enter a string: ")
first = sentence[0]
last = sentence[-1]
middle = sentence[1:-1]

print("First and last letter interchanged is:", last + middle + first)
