dict1 = {}
dict2 = {}

m = int(input("Enter no. of entries to dict1: "))
for i in range(m):
	key = input("Enter key: ")
	value = input("Enter value: ")
	dict1[key] = value

n = int(input("Ente no. of entries to dict2: "))
for i in range(n):
	key = input("Enter keys: ")
	value = input("Enter value: ")
	dict2[key] = value

merged_dict = {**dict1, **dict2}
print("Merged dict is", merged_dict)
