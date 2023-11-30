# Приклад №1 ################################################################################
print('Приклад №1:\n')

def ispalindrom(text):
    text = text.replace(" ", "").lower()
    if text == text[::-1]:
        print("It's a palindrom")
    else:
        print("It's not a palindrom")

text = input("Введіть текст:")
ispalindrom(text)

text = input("Введіть текст:")
ispalindrom(text)

# Приклад №2 ################################################################################
print('\nПриклад №2:\n')

# Пеервірка на анаграму

text1 = input("Введіть перше слово:")
text2 = input("Введіть друге слово:")

text1 = list(text1.replace(" ", "").lower())
text2 = list(text2.replace(" ", "").lower())

if sorted(text1) == sorted(text2):
    print("Анаграми")
else:
    print("Не анаграми")

# Приклад №3 ################################################################################
print('\nПриклад №3:\n')

# Обчислює число "життя": суму цифр повної дати народження
date = input("Введіть дату народження у форматі YYYYMMDD:")

while True:
    summ = 0
    for simbol in date:
        summ += int(simbol)

    date = str(summ)

    if len(date) == 1:
        break

print(summ)

# Приклад №4 ################################################################################
print('\nПриклад №4:\n')

while True:
    try: 
        number = int(input(" Введіть ціле число: ")) 
        print(number/2) 
        break 
    except: 
        print("Введене значення не є допустимим числом. Повторіть спробу...")

# Завдання №1 ###############################################################################
print('\nЗавдання №1:\n')

def is_hidden(word, string):
    current_index = 0

    for char in word:
        current_index = string.find(char, current_index)
        if current_index == -1:
            return 'No'
        current_index += 1

    return 'Yes'

string1 = "vcxzxduybfdsobywuefgas"
string2 = "vcxzxdcybfdstbywuefsas"
word_to_find = "dog"

result1 = is_hidden(word_to_find, string1)
result2 = is_hidden(word_to_find, string2)

print (result1)
print (result2)

# Завдання №2 ###############################################################################
print('\nЗавдання №2:\n')

while True:
    try:
        date = input("Введіть дату народження у форматі YYYYMMDD: ")
        if not date.isdigit() or len(date) != 8:
            raise ValueError("Некоректний формат дати.")

        total_sum = sum(int(symbol) for symbol in date)

        while total_sum >= 10:
            total_sum = sum(int(symbol) for symbol in str(total_sum))

        print(total_sum)
        break

    except ValueError as e:
        print(e)

# Завдання №3 ###############################################################################
print('\nЗавдання №3:\n')

def check_input(prompt, min_value, max_value):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < min_value or user_input > max_value:
                raise ValueError(f"Error: the value {user_input} is not within permitted range ({min_value}..{max_value})")
            return user_input
        except ValueError as e:
            if e.args[0].startswith("invalid literal for int()"):
                print("Error: wrong input")
            else:
                print(e)

# Запит користувача для введення min_value та max_value
min_value = int(input("Введіть мінімальне значення: "))
max_value = int(input("Введіть максимальне значення: "))

# Приклад використання функції з введеними користувачем min_value та max_value
result = check_input("Введіть число: ", min_value, max_value)
print(f"Ваше число: {result}")


