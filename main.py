import queue
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

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
def process_numbers(q, total_steps, count, lock):
    while not q.empty():
        try:
            number = q.get_nowait()
            steps = collatz_steps(number)
            # Використовуємо Lock для захисту доступу до змінних
            with lock:
                total_steps[0] += steps
                count[0] += 1
        except queue.Empty:
            break

def main():
    # Параметри
    num_threads = 8
    max_number = 1000  # Менше для тестування

    # Черга для чисел
    number_queue = queue.Queue()
    for i in range(1, max_number + 1):
        number_queue.put(i)

    # Ініціалізація змінних
    total_steps = [0]  # Використання списку як контейнера для зміни значень всередині потоків
    count = [0]
    lock = Lock()  # Блокування для захисту спільних змінних

    # Використовуємо ThreadPoolExecutor для створення потоків
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(process_numbers, number_queue, total_steps, count, lock) for _ in range(num_threads)]
        for future in futures:
            future.result()

    # Обчислення середньої кількості кроків
    average_steps = total_steps[0] / count[0] if count[0] > 0 else 0
    print(f"Середня кількість кроків: {average_steps}")

if __name__ == "__main__":
    main()
