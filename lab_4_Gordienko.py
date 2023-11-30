# Завдання №1 ###############################################################################
print('Завдання №1:\n')

num = int(input('Введіть число: '))
print(num >= 100)

# Завдання №2 ###############################################################################
print('\nЗавдання №2:\n')

num1 = int(input('Введіть перше число: '))
num2 = int(input('Введіть друге число: '))
if num1 > num2:
    print(f'{num1} > {num2}')
elif num1 == num2:
    print(f'{num1} = {num2}')
else:
    print(f'{num1} < {num2}')

# Завдання №3 ###############################################################################
print('\nЗавдання №3:\n')

print('Напишіть cлово Spathiphyllum або spathiphyllum:')
flower = input()
if flower == 'Spathiphyllum':
    print('Yes - Spathiphyllum is the best plant ever!')
elif flower == 'spathiphyllum':
    print('No, I want a big Spathiphyllum!')
else:
    print(f'Spathiphyllum! Not {flower}!')

# Завдання №4 ###############################################################################
print('\nЗавдання №4:\n')

income = float(input("Enter the annual income: "))
if income < 85528.00:
    tax = (income / 100) * 18 - 556.02
    if tax < 0:
        tax = 0
else:
    tax = (income / 100) * 32 + 14839.02
tax = round(tax, 0)
print("The tax is:", tax, "thalers")

# Завдання №5 ###############################################################################
print('\nЗавдання №5:\n')

year = int(input('Enter the year: '))
if year < 1582:
    print('Not withil the Gregorian calendar period.')
elif (year % 4) != 0:
    if (year % 100) != 0:
        print('Leap year')
    elif (year % 400) != 0:
        print('Common year')
else:
    print('Leap year')

# Завдання №6 ###############################################################################
print('\nЗавдання №6:\n')

secret_number = 69
print(
"""
+================================+
| Welcome to my game, muggle!            |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    x = int(input('Вгадай секретне число: '))
    if x == secret_number:
        print('Молодець, магле! Тепер ти вільний!')
        break
    else:
        print('Ха-ха! Ви застрягли у моїй петлі!')

# Завдання №7 ###############################################################################
print('\nЗавдання №7:\n')

import time
for x in range(1, 6):
    print(f'{x} Mississippi!')
    time.sleep(1)
print('Ready or not, here I come!')

# Завдання №8 ###############################################################################
print('\nЗавдання №8:\n')

while True:
    word = input('Enter the word: ')

    if word == 'chupacabra':
        print('You\'ve successfully left the loop.')
        break

# Завдання №9 ###############################################################################
print('\nЗавдання №9:\n')

user_word = input('Enter the word: ')
user_word = user_word.upper()
for letter in user_word:
    if letter in 'AEIOU':
        continue
    print(letter)

# Завдання №10 ###############################################################################
print('\nЗавдання №10:\n')

user_word = input('Enter the word: ')
user_word = user_word.upper()
word_without_vowels = ''
for letter in user_word:
    if letter in 'AEIOU':
        continue
    word_without_vowels += letter
print(word_without_vowels)

# Завдання №11 ###############################################################################
print('\nЗавдання №11:\n')

blocks = int(input('Enter the number of blocks: '))
counter = 0
while blocks > 0:
    blocks -= counter + 1
    counter += 1
    if (counter + 1) > blocks:
        break
print('The height of the pyramid: ', counter)

# Завдання №12 ###############################################################################
print('\nЗавдання №12:\n')

def collats(num, counter = 0):
    if num % 2 == 0:
        num /= 2
    else:
        num = 3 * num + 1
    counter += 1
    print(int(num))
    if num != 1:
        collats(num, counter)
    else:
        print(f'steps = {counter}')
collats(int(input('Enter the number: ')))