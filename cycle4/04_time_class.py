class Time:
    def __init__(self, h, m, s):
        self.seconds = s%60
        self.minutes = (m + s//60)%60
        self.hours = (h + m//60 + s//3600)

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def __add__(self, other):
        return Time(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)

t1 = Time(10, 20, 20)
t2 = Time(5, 50, 50)

t3 = t1 + t2

print(t3)
