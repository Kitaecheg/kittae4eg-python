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
n1 = int(input('з якого числа починається диапазон?: '))
n2 = int(input('яким числом закінчується диапазон?: '))
for i in range(n1, n2):
    j = 2
    is_prime = 0  # Переменная для проверки простоты числа
    while j <= (i / 2):  # Проверяем делители до i / 2
        if i % j == 0:  # Если число делится на j, то оно не простое
            is_prime = 1
            break  # Выходим из цикла, т.к. нашли делитель
        j = j + 1  # Переходим к следующему делителю
    if is_prime == 0:  # Если делителей не нашлось, число простое
        print(i, 'простое число')