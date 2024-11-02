import threading
import queue
from concurrent.futures import ThreadPoolExecutor

# Функція для обчислення кроків для виродження в 1 за гіпотезою Колаца
def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

# Функція для обробки чисел з черги
def process_numbers(q, result_q):
    while not q.empty():
        try:
            number = q.get_nowait()
            steps = collatz_steps(number)
            result_q.put(steps)
        except queue.Empty:
            break

def main():
    # Параметри
    num_threads = 8  # Кількість потоків для паралельного обчислення
    max_number = 10_000_000  # Максимальне число

    # Черги для чисел та результатів
    number_queue = queue.Queue()
    result_queue = queue.Queue()

    # Заповнюємо чергу числами
    for i in range(1, max_number + 1):
        number_queue.put(i)

    # Використовуємо ThreadPoolExecutor для створення потоків
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(process_numbers, number_queue, result_queue) for _ in range(num_threads)]
        # Чекаємо завершення всіх потоків
        for future in futures:
            future.result()

    # Підраховуємо середню кількість кроків
    total_steps = 0
    count = 0
    while not result_queue.empty():
        total_steps += result_queue.get()
        count += 1

    average_steps = total_steps / count if count > 0 else 0
    print(f"Середня кількість кроків: {average_steps}")

if __name__ == "__main__":
    main()
