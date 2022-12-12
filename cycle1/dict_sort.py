n = int(input("Enter no. of entries into dictionary: "))
my_dict = {}
for i in range(n):
	key = input("Enter key: ")
	value = input("Enter value: ")

	my_dict[key] = value

sorted_dict = sorted(my_dict.items(), key=lambda x: x[0])
desc_sorted_dict = sorted(my_dict.items(), key=lambda x: x[0], reverse=True)

print("Ascending:", sorted_dict)
print("Descending:", desc_sorted_dict)
