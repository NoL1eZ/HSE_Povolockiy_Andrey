import datetime
# как мне кажется следует сделать задание 2
def seconds_conveter ():
    input_seconds = input("Введите время в секундах: ")
    if input_seconds.isdigit():
        return datetime.timedelta(seconds=int(input_seconds))
    else:
        return 'Время измеряется в цифрах'

# комментирую через ctrl+/
# 1.	Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, а затем выведите на экран.
# Используйте функции для консольного ввода input() и консольного вывода print().
#
# Попробуйте также через встроенную функцию id() понаблюдать, какие типы объектов могут изменяться и сохранять за собой адрес в оперативной памяти.


variable1 = ("Skoda Oktavia_1", "Mercedes-Benz G-Class_1", "Rolls-Royce Phantom", "Mercedes-Benz G-Class_2", "Skoda Oktavia_2")
variable2 = "Hello, World!"
variable3 = 3.14

print("Переменные:")
print("variable1:", variable1)
print("variable2:", variable2)
print("variable3:", variable3)

user_number = int(input("Введите число: "))
user_string = input("Введите строку: ")

print("Вы ввели число:", user_number)
print("Вы ввели строку:", user_string)

print("ID переменной variable1:", id(variable1))
print("ID переменной variable2:", id(variable2))
print("ID переменной variable3:", id(variable3))
print("ID переменной user_number:", id(user_number))

# 2.	Пользователь вводит время в секундах. Рассчитайте время и сохраните отдельно в каждую переменную количество часов, минут и секунд.
# Переведите время в часы, минуты, секунды и сохраните в отдельных переменных.
#
# Используйте приведение типов для перевода строк в числовые типы.
# Предусмотрите проверку строки на наличие только числовых данных через встроенный строковый метод .isdigit().
#
# Выведите рассчитанные часы, минуты и секунды по отдельности в консоль.


def seconds_conveter_1 ():
    input_seconds = input("Введите время в секундах: ")
    if input_seconds.isdigit():
        total_seconds = int(input_seconds)

        hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60

        print("Введенное время в формате ЧЧ:ММ:СС:")
        print(f"Часы: {hours}")
        print(f"Минуты: {minutes}")
        print(f"Секунды: {seconds}")
    else:
        return "Ошибка: Введите только цифры."

print(seconds_conveter())
print(seconds_conveter_1())

# 3.	Запросите у пользователя через консоль число n (от 1 до 9). Найдите сумму чисел n + nn + nnn.
#
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
#
# Выведите данные в консоль.
input_n = input("Введите n: ")
print(int(input_n+input_n+input_n)+int(input_n+input_n)+int(input_n))