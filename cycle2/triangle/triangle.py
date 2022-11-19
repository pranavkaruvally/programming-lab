def make_triangle():
    for i in range(1, 10):
        if i <= 5:
            for x in range(i):
                print("*", end=' ')
            print()
        else:
            for x in range(10-i):
                print("*", end=' ')
            print()

make_triangle()
