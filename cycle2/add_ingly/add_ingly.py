def add_ing(s):
    s += 'ing'
    return s

def add_ly(s):
    s += 'ly'
    return s

def add_appropriately(s):
    if s[-3:] == 'ing':
        return add_ly(s)
    return add_ing(s)

s = input("Enter string: ")
print(add_appropriately(s))
