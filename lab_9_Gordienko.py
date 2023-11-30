# Приклад №1 ################################################################################
print('Приклад №1:\n')

def mysplit(string):
    list_split = []
    word = ""

    for char in string:
        if char == " ":
            if word:
                list_split.append(word)
                word = ""
        else:
            word += char

    if word:
        list_split.append(word)

    return list_split

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

# Приклад №2 ################################################################################
print('\nПриклад №2:\n')

number_input = int(input('Введіть ціле число: '))
number_list = [str(i) for i in range(0, 10)]

number_dict = {'1' : ('  #', '  #', '  #', '  #', '  #'),
               '2' : ('###', '  #', '###', '#  ', '###'),
               '3' : ('###', '  #', '###', '  #', '###'),
               '4' : ('# #', '# #', '###', '  #', '  #'),
               '5' : ('###', '#  ', '###', '  #', '###'),
               '6' : ('###', '#  ', '###', '# #', '###'),
               '7' : ('###', '  #', '  #', '  #', '  #'),
               '8' : ('###', '# #', '###', '# #', '###'),
               '9' : ('###', '# #', '###', '  #', '###'),
               '0' : ('###', '# #', '# #', '# #', '###')
               }
def display_number(num):
    if num < 0:
        print("Число має бути невід'ємним.")
        return

    num_str = str(num)

    for level in range(5):
        for simbol in num_str:
            print(number_dict[simbol][level], end=' ')
        print()

display_number(number_input)


# Приклад №3 ################################################################################
print('\nПриклад №3:\n')

text = input("Введіть текст для шифрування (англійською): ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

# Приклад №4 ################################################################################
print('\nПриклад №4:\n')

cipher = input('Введіть текст для дешифрування (англійською): ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)

# Завдання №1 ###############################################################################
print('\nЗавдання №1:\n')

def get_valid_shift():
    while True:
        try:
            shift = int(input("Введіть значення зсуву (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Зсув повинен бути в межах від 1 до 25. Будь ласка, спробуйте знову.")
        except ValueError:
            print("Некоректне значення. Будь ласка, введіть дійсне число.")

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Визначаємо регістр літери (верхній або нижній)
            is_upper = char.isupper()
            # Зміщення символу у регістрі ASCII
            shifted = ord(char) + shift
            # Перевірка, чи символ за межами діапазону a-z/A-Z
            if is_upper and shifted > ord('Z'):
                shifted -= 26
            elif not is_upper and shifted > ord('z'):
                shifted -= 26
            # Додаємо зашифрований символ до результату
            encrypted_text += chr(shifted)
        else:
            # Неалфавітні символи додаємо без змін
            encrypted_text += char
    return encrypted_text

def caesar_cipher_user_input():
    text = input("Введіть текст для шифрування (англійською): ")
    shift = get_valid_shift()
    encrypted_text = caesar_cipher(text, shift)
    print("Зашифрований текст:", encrypted_text)

caesar_cipher_user_input()