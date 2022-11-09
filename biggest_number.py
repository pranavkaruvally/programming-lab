a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = c if c > (a if a>b else b) else (a if a>b else b)

print(largest)
