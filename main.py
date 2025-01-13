import threading
import math

# Функція для обчислення факторіалу
def calculate_factorial(n):
    print(f"Обчислюємо факторіал для {n}")
    result = math.factorial(n)
    print(f"Факторіал {n} = {result}")

# Функція для обчислення степенів числа
def calculate_power(base, exponent):
    print(f"Обчислюємо {base} в степені {exponent}")
    result = math.pow(base, exponent)
    print(f"{base}^{exponent} = {result}")

# Створюємо потоки для виконання обчислень
thread1 = threading.Thread(target=calculate_factorial, args=(10,))
thread2 = threading.Thread(target=calculate_power, args=(2, 10))

# Запускаємо потоки
thread1.start()
thread2.start()

# Очікуємо завершення обох потоків
thread1.join()
thread2.join()

print("Обчислення завершено")
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
