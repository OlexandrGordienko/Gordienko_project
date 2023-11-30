# Завдання №1 ###############################################################################
print('Завдання №1:\n')

numbers = (1, 5, 8, 3, 12, 4, 10, 7, 2, 15)
n = int(input("Введіть число n: "))
result = [num for num in numbers if num < n]
print("Числа, які менші за", n, ":", result)
        
# Завдання №2 ###############################################################################
print('\nЗавдання №2:\n')

my_tuple = ("Gordienko", "Sydorenko", "Python")
print(','.join(my_tuple))
        
# Завдання №3 ###############################################################################
print('\nЗавдання №3:\n')

library = {
    "Тигролови": {"author": "Іван Багряний", "year": 1926, "pages": 264},
    "Кобзар": {"author": "Тарас Шевченко", "year": 1835, "pages": 720},
    "Майстер і Маргарита": {"author": "Михайло Булгаков", "year": 1967, "pages": 384},
}

book_name = input("Введіть назву книги: ")

if book_name in library:
    book_info = library[book_name]
    print(f"Автор: {book_info['author']}\nРік видання: {book_info['year']}\nКількість сторінок: {book_info['pages']}")
else:
    print("Книги з такою назвою немає в бібліотеці.")
        
# Завдання №4 ###############################################################################
print('\nЗавдання №4:\n')

students = {
    "Гордієнко": ("Олександр", 19, "Комп'ютерна інженерія"),
    "Герасименко": ("Владислав", 20, "Середня освіта інформатика"),
    "Бублик": ("Іван", 18, "Комп'ютерні науки"),
}

surname = input("Введіть прізвище студента: ")

if surname in students:
    student_info = students[surname]
    print(f"Ім'я: {student_info[0]}\nВік: {student_info[1]}\nСпеціальність: {student_info[2]}")
else:
    print("Студента з таким прізвищем немає.")
        
# Завдання №5 ###############################################################################
print('\nЗавдання №5:\n')

def add_phone_number(contacts, contact_name, new_phone_number):
    if contact_name in contacts:
        contacts[contact_name].append(new_phone_number)
        print(f"Новий номер телефону {new_phone_number} доданий для контакту {contact_name}.")
    else:
        print(f"Контакту {contact_name} немає в телефонній книзі.")
phonebook = {
    "Олександр": ["+380982339699", "+38066567456"],
    "Владислав": ["+38066676775", "+38034546331"],
    "Валерій": ["+380989898989", "+380675474453"],
}
add_phone_number(phonebook, input('Введіть ім\'я: '), input('Введіть номер: '))
print("\nСписок номерів телефонів для всіх контактів:")
for contact, phone_numbers in phonebook.items():
    print(f"{contact}: {phone_numbers}")