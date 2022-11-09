color_sentence1 = input("Enter colors seperated by spaces: ")
color_sentence2 = input("Enter colors seperated by spaces: ")

color_list1 = color_sentence1.split()
color_list2 = color_sentence2.split()

difference_list = [x for x in color_list1 if x not in color_list2]
print("Colors in list1 not in list2: ", difference_list)
