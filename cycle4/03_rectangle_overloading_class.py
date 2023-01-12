class Rectangle:
    def __init__(self, l, b):
        self.__length = l
        self.__breadth = b
    def area(self):
        return self.__length * self.__breadth
    def perimeter(self):
        return 2*(self.__length + self.__breadth)

    def __lt__(self, other):
        return self.area() < other.area()

if __name__ == "__main__":
    l1 = int(input("Enter length: "))
    b1 = int(input("Enter breadth: "))
    r1 = Rectangle(l1, b1)

    l2 = int(input("Enter length: "))
    b2 = int(input("Enter breadth: "))
    r2 = Rectangle(l2, b2)

    if r1 < r2:
        print("Rectangle r1 has lesser area")
    else:
        print("Area of rectangle r1 is greater than or equal to that of r2")
