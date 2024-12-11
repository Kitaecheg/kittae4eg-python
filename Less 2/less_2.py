#string
s1 = "some string"
print(s1)
#intrger
num1 = 123
print(num1)
#float
num_f = 3.1
print(num_f)
#bool
b = False
print(b)
#list
l = [1, 2, "hi", 6]
print(l)
#dict
d = {1, 2, 3, "qwerty", 9}
print(d)
#tuple
first_tuple = (1, 2, 3, 4, "yes", "no")
print(first_tuple)
#None
n = None
print(n)

num2 = 1123
num3 = 12
print(num2 == num3)

str_1 = "qwerty"
str_2 = "hello"

print(str_1 == str_2)

print(f"Строка 1 не дорівнює строці та число 2 не дорівнює числу 3: ------> {str_1 != str_2 and num2 != num3}")

#Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()
num_str = 125
print(type(str(num_str)))
str_num = str(num_str)
print(type(str_num))

#Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити  
#усі букви 'y' на '0' та 'i' на '1'.
message = 'Hi, my name is Python!'
print(message)
mess1 = message.replace('y', '0').replace('i', '1')
print(mess1)

#Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за 
#допомогою функції split(), 
#а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join
split_test = 'This is a split test'
print(split_test)
split_test = split_test.split()
print(split_test)
string_join = " ".join(split_test)
print(string_join)
#Визначити довжину рядку string_join за допомогою функції len()
print("довжина рядка string_join: ", len(string_join))

#Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print("розширений список list_append: ", list_append)

#Cтворити змінну list_extend = [4, 5, 6] 
# і розширити цей список іншим списком [7, 8, 9] за допомогою функції extend()
list_extend = [4, 5, 6]
print(list_extend)
list_extend.extend([7, 8, 9])
print(list_extend)

#Визначити індекс елемента 6 у списку list_extend за допомогою функції index()
print(list_extend.index(6))

#Визначити довжину списку list_append за допомогою функції len()
print("довжинa списку list_append: ", len(list_append))


#Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} 
# та вивести на екран дані, які знаходяться в ключах car та where
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test.values())
print(dict_test.get('car', 'no key, try again'), '------>', dict_test.get('where', 'no key, try again'))

#За допомогою функцій keys() і values() вивести на екран ключі та їх значення
dict_1 = {'Name': 'Myk', 'Edge': 38}
print(dict_1.values())
print(dict_1.keys())

#а допомогою функції items() вивести на екран пари ключ - значення
print(dict_1.items())