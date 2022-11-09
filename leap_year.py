def is_leap_year(year):
    if year%1000 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False

current_year = int(input("Enter current year: "))
final_year = int(input("Enter final year: "))

for year in range(current_year, final_year+1):
    if is_leap_year(year):
        print(year)
