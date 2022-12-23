from graphics import *

print("___RECTANGLE__")
l = int(input("Length: "))
b = int(input("Breadth: "))
print(f"Perimter: {rectangle.perimeter(l,b)}\nArea: {rectangle.area(l, b)}")

print("__CIRCLE__")
r = int(input("Radius: "))
print(f"Circumference: {circle.perimeter(r)}\nArea: {circle.area(r)}")

print("__CUBOID__")
l = int(input("Length: "))
b = int(input("Breadth: "))
h = int(input("Height: "))
print(f"Surface Area: {cuboid.total_surface_area(l, b, h)}\nVolume: {cuboid.volume(l, b, h)}")

print("__SPHERE__")
r = int(input("Radius: "))
print(f"Surface Area: {sphere.surface_area(r)}\nVolume: {sphere.volume(r)}")
