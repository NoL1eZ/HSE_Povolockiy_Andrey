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
print("ID переменной user_string:", id(user_string))