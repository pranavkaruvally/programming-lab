first = list(input("Enter first string: "))
second = list(input("Enter second string: "))

first[1], second[1] = second[1], first[1]
final = ''.join(first) + ' '  +  ''.join(second)

print(final)
