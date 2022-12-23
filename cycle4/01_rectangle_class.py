class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2*(self.length + self.breadth)

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

if __name__ == "__main__":
    l1 = int(input("Enter length: "))
    b1 = int(input("Enter breadth: "))
    r1 = Rectangle(l1, b1)

    l2 = int(input("Enter length: "))
    b2 = int(input("Enter breadth: "))
    r2 = Rectangle(l2, b2)

    if (r1 == r2):
        print("The rectangles are equal in Area")
    elif r1 < r2:
        print("Rectangle r2 has greater area")
    else:
        print("Rectangle r1 has greater area")
