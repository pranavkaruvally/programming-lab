class Time:
    def __init__(self, h, m, s):
        self.__sec = s%60
        self.__mts = (m + s//60)%60
        self.__hrs = (h + m//60 + s//3600)

    def __str__(self):
        return f"{self.__hrs}:{self.__mts}:{self.__sec}"

    def __add__(self, other):
        return Time(self.__hrs + other.__hrs, self.__mts + other.__mts, self.__sec + other.__sec)

t1 = Time(10, 20, 20)
t2 = Time(5, 50, 50)

t3 = t1 + t2

print(t3)
