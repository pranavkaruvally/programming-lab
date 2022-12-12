num_string = input("Enter a list of integers seperated by spaces: ")
nums = list(map(int, num_string.split()))

non_even_list = [x for x in nums if x%2 == 1]
print("The list not including even numbers are", end=" ")
[print(x, end=" ") for x in non_even_list]
print()
