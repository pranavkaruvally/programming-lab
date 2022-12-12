#This program calculates the area and perimeter of a circle

PI = 3.141592653589793

radius = float(input("Enter the radius of the circle: "))
area = PI*radius*radius
perimeter = 2*PI*radius

print("The area of the circle is", area, "units")
print("The perimeter of the circle is", perimeter, "units")
