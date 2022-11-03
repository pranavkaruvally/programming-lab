input_string = input("Enter a list of integers seperated by spaces")
input_list = list(map(int, input_string.split()))
input_list = ['over' if x > 100 else x for x in input_list]
print(input_list)
