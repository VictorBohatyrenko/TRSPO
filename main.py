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
