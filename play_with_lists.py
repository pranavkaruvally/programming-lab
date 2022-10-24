#Three objectives
#Check whether lists are of same length
#Check whether the two lists sum upto the same value
#Check whether any value occur in both lists

list1 = input("Enter the required numbers seperated by spaces").split()
list1 = list(map(int, list1))

list2 = input("Enter the required numbers seperated by spaces").split()
list2 = list(map(int, list2))

if len(list1) == len(list2):
    print("The lists are of same length")
else:
    print("The lists are of different length")

if sum(list1) == sum(list2):
    print("The lists sum upto the same value")
else:
    print("The lists do not sum upto the same value")

for number in list1:
    if number in list2:
        print("Both lists have common values")
        break
else:
    print("The lists do not have any common values")

'''
The above given for-else loop can be replaced with a simple for loop along with a flag as given below

flag = False

for number in list1:
    if number in list2:
        print("Both lists have common values")
        flag = True
        break

if flag == False:
    print("The lists do not have a value in common")
'''

