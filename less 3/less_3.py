### Умовні конструкції:
'''1. **Перевірка паролю:**
   Завдання: Напишіть програму, яка встановлює початковий пароль і перевіряє, 
   чи введений користувачем пароль співпадає з ним. Якщо пароль дорівнює "password123", 
   виведіть повідомлення "Ви увійшли в систему". 
   В іншому випадку виведіть повідомлення "Неправильний пароль".'''
'''
p = input("Введіть пароль: ")
if p == 'password123':
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")
'''
    
'''
2. **Визначення днів тижня:**
   Завдання: Створіть програму, яка встановлює номер дня тижня і виводить назву відповідного дня тижня. 
   Якщо номер дня недійсний (менше 1 або більше 7), виведіть повідомлення про помилку. 
   '''  

'''
day_of_week = ['Понеділок', 'Вівторок', 'Середа', 'Черверг', 'П\'ятниця', 'Субота', 'Неділя']
n = int(input("Введыть номер дня тижня: "))
if n >= 1 or n <= 7:
    print(day_of_week[n-1])
else:
    print("Не вірно вказаний номер дня тижня, введіть число від 1 до 7")
'''
    
### Цикли:
'''
1. **Таблиця множення:**
   Завдання: Виведіть таблицю множення для заданого числа від 1 до 10.
'''   
'''
lst_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s1 = int(input("введіть число: "))
s2 = input('введіть оператор: ')
if s2 == "*":
    for num in lst_count:
        print(s1," * ",num, "= ", s1*num)
elif s2 == "+":
    for num in lst_count:
        print(s1," + ",num, "= ", s1+num)
elif s2 == "-":
    for num in lst_count:
        print(s1," - ",num, "= ", s1-num)
elif s2 == "/":
    for num in lst_count:
        print(s1," / ",num, "= ", s1/num)
'''
        

'''
**Сума чисел:**
   Завдання: Визначте список чисел і обчисліть їх суму.
'''
'''
lst_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(lst_count)) 
lst_sum = 0
for cs in lst_count:
    lst_sum += cs
print(lst_sum)
'''


'''
**Факторіал числа:**
   Завдання: Обчисліть факторіал заданого числа.
'''
'''
f = int(input('Введіть ціле число для обчислення факторіалу: '))
fac = 1
s = 1
while s <= f:
    fac *= s
    s+=1
print(f"Факторіал числа {f} = {fac}")
'''

'''
**Парні числа:**
   Завдання: Виведіть всі парні числа від 1 до 50.
'''
'''
a = 1
while a <= 50:
    if a%2 == 0:
        print(a)
    a += 1
'''

'''
**Пошук простих чисел:**
   Завдання: Знайдіть всі прості числа в заданому діапазоні.
Створіть власні змінні або встановіть початкові значення, 
щоб виконати ці завдання без використання `input`.
Використовуйте умовні конструкції і цикли для розв'язання кожного завдання.
'''
# n1 = int(input('з якого числа починається диапазон?: '))
# n2 = int(input('яким числом закінчується диапазон?: '))
# for i in range(n1, n2):
#     j = 2
#     is_prime = 0 
#     while j <= (i / 2):  
#         if i % j == 0:  
#             is_prime = 1
#             break
#         j = j + 1
#     if is_prime == 0:
#         print(i, 'просте число')



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
    else:
        print("Страна не найдена в списке.")
    
        