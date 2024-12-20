### Списки:
'''
1. **Робота із списками:**
   Завдання: Створіть список чисел. 
   Додайте до списку числа 10 і 20, видаліть число 10 і виведіть отриманий список.
'''

# lst1 = [1, 2, 3, 4, 5, 6]
# lst1 += [10, 20]
# print(lst1)
# lst1.remove(10)
# print(lst1)

'''**Знаходження суми:**
   Завдання: Створіть список чисел. Знайдіть та виведіть суму всіх чисел у списку.
'''
# lst1 = [1, 2, 3, 4, 5, 6]
# print(sum(lst1))


'''**Подвійні значення:**
   Завдання: Створіть список чисел. Подвойте кожне число у списку та виведіть результат.
'''
# lst1 = [1, 2, 3, 4, 5, 6]
# n = len(lst1)
# c = 0

# while c < n:
#     lst1[c] = lst1[c] * 2
#     c += 1
# print(lst1)

### Кортежі:
'''
1. **Робота із кортежами:**
   
   Завдання: Створіть кортеж з трьох різних предметів, 
   таких як ("яблуко", "банан", "апельсин"). Виведіть кожен елемент кортежу окремо.
'''
# fruits_tuple = ("яблуко", "банан", "апельсин")
# print(fruits_tuple[0], fruits_tuple[1], fruits_tuple[2])


'''
**Об'єднання кортежів:**
   Завдання: Створіть два кортежі з числами і об'єднайте їх у новий кортеж. Виведіть отриманий кортеж.
'''

# fruits_tuple = ("яблуко", "банан", "апельсин")
# price_tuple = ("123", "234", "567")
# new_tuple = fruits_tuple + price_tuple
# print(new_tuple)

### Словники:
'''
1. **Робота із словниками:**
   Завдання: Створіть словник, що містить інформацію про вашого улюбленого спортсмена 
   (ім'я, вік, спорт, команда тощо). Виведіть цю інформацію на екран.
'''

# favorite = {
#     'name':' Michael Gerard Tyson',
#     'sport':'boxer',
#     'birth':'30.06.1966',
#     'last fight':'15.11.2024',
# }
# print(favorite)


'''
**Пошук значення:**
   Завдання: Створіть словник, що містить інформацію про країни та їх столиці. 
   Запитайте користувача про назву країни і виведіть столицю цієї країни (якщо така країна є у словнику).
   Завершіть кожне завдання, використовуючи вбудовані методи для списків, кортежів та словників.
    Бажаю успіхів у виконанні цих завдань!
'''


countries_and_capitals = [
    ("Россия", "Москва"),
    ("США", "Вашингтон"),
    ("Франция", "Париж"),
    ("Германия", "Берлин"),
    ("Италия", "Рим"),
    ("Япония", "Токио"),
    ("Китай", "Пекин"),
    ("Испания", "Мадрид"),
    ("Канада", "Оттава"),
    ("Австралия", "Канберра")
]
country_input = input("Введите название страны: ")
for country, capital in countries_and_capitals:
    if country_input == country:
        print(country, capital)
        break
