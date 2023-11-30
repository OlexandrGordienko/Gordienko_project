# Завдання №1 ###############################################################################
print('Завдання №1:\n')

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
        
# Завдання №2 ###############################################################################
print('\nЗавдання №2:\n')

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_year_leap(year) and month == 2:
        return 29
    else:
        return month_days[month]


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

# Завдання №3 ###############################################################################
print('\nЗавдання №3:\n')

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_year_leap(year) and month == 2:
        return 29
    else:
        return month_days[month]
    
def day_of_year(year, month, day):
    total_days = day
    for m in range(1, month):
        total_days += days_in_month(year, m)
    return total_days

print(day_of_year(2000, 12, 31))


# Завдання №4 ###############################################################################
print('\nЗавдання №4:\n')

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()

# Завдання №5 ###############################################################################
print('\nЗавдання №5:\n')

mile = 1.609344
gallon = 3.785411784
liter = 0.264172
km = 0.621371

def liters_100km_to_miles_gallon(liters):
    mpg = (100 * km) / (liters * liter)
    return mpg

def miles_gallon_to_liters_100km(miles_per_gallon):
    l_100km = (100 * km) / (miles_per_gallon * liter)
    return l_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

# Завдання №6 ###############################################################################
print('\nЗавдання №6:\n')

def is_a_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

side1 = 3
side2 = 4
side3 = 5

result = is_a_triangle(side1, side2, side3)
if result:
    print(f"Зі сторонами {side1}, {side2}, {side3} можна побудувати трикутник.")
else:
    print(f"Зі сторонами {side1}, {side2}, {side3} не можна побудувати трикутник.")

# Завдання №7 ###############################################################################
print('\nЗавдання №7:\n')

def is_a_right_triangle(a, b, c):
    if is_a_triangle(a, b, c):
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return True
    return False

result = is_a_right_triangle(side1, side2, side3)
if result:
    print(f"Трикутник із сторонами {side1}, {side2}, {side3} є прямокутним.")
else:
    print(f"Трикутник із сторонами {side1}, {side2}, {side3} не є прямокутним.")