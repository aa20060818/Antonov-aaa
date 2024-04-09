# Калькулятор на Python

# Функция для сложения
def add(x, y):
    return x + y

# Функция для вычитания
def subtract(x, y):
    return x - y

# Функция для умножения
def multiply(x, y):
    return x * y

# Функция для деления
def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    return x / y

# Вывод возможных операций
print("Доступные операции:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

# Ввод операции
choice = input("Выберите операцию (1/2/3/4): ")

# Ввод чисел
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Выполнение выбранной операции
if choice == '1':
    print("Результат:", add(num1, num2))

elif choice == '2':
    print("Результат:", subtract(num1, num2))

elif choice == '3':
    print("Результат:", multiply(num1, num2))

elif choice == '4':
    print("Результат:", divide(num1, num2))

else:
    print("Неверный выбор операции")
