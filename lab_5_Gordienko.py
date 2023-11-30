# Завдання №1 ###############################################################################
print('Завдання №1:\n')

hat_list = [1, 2, 3, 4, 5]  
user_input = int(input("Введіть число яким замінимо середнє масива: "))
hat_list[len(hat_list) // 2] = user_input

hat_list.pop()
print("Довжина списку:", len(hat_list))
print(hat_list)

# Сортування списків ########################################################################
print('\nЗСортування списків:\n')

list = [4, 97, 13, 0, 69]
list.sort()
print(list)
list.reverse()
print(list)

# Завдання №2 ###############################################################################
print('\nЗавдання №2:\n')

n = int(input("Введіть кількість елементів у списку: "))
my_list = []

for i in range(n):
    element = int(input(f"Введіть елемент {i+1}: "))
    my_list.append(element)

print("Список до сортування:", my_list)

for i in range(n):
    for j in range(0, n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

print("Список після сортування методом бульбашки:", my_list)

# Завдання №3 ###############################################################################
print('\nЗавдання №3:\n')

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

unique_list = []
for num in my_list:
    if num not in unique_list:
        unique_list.append(num)

print("The list with unique elements only:")
print(my_list)

# Завдання №4 ###############################################################################
print('\nЗавдання №4:\n')

chessboard = [['_'] * 8 for _ in range(8)]

chessboard[0][0] = 'T' 
chessboard[0][7] = 'T'
chessboard[7][0] = 'T'
chessboard[7][7] = 'T'

for row in chessboard:
    print(' '.join(row))