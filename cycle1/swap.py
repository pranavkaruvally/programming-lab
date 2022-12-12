#This program swaps the values of two variables

a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))
print("a=%d, b=%d" %(a, b))
print("Swapping...")
a, b = b, a
print("a=%d, b=%d" %(a, b))
