# server.py
import socket
import numpy as np
from concurrent.futures import ThreadPoolExecutor

# Функція для перемноження матриць
def multiply_matrices(matrix_a, matrix_b):
    return np.dot(matrix_a, matrix_b)

# Обробка клієнтського запиту
def handle_client(client_socket):
    try:
        # Отримання розмірів матриць
        sizes = client_socket.recv(1024).decode('utf-8').strip().split(',')
        n, m, l = map(int, sizes)
        print(f"Received matrix sizes: N={n}, M={m}, L={l}")

        # Отримання матриць
        data_size = n * m + m * l
        data = bytearray()
        while len(data) < data_size * 8:  # Очікуємо всі байти
            packet = client_socket.recv(1024 * 1024)
            if not packet:
                break
            data.extend(packet)

        matrices = np.frombuffer(data, dtype=np.float64)
        matrix_a = matrices[:n * m].reshape((n, m))
        matrix_b = matrices[n * m:].reshape((m, l))
        print(f"Received matrices A({n},{m}) and B({m},{l})")

        # Перемноження матриць
        result = multiply_matrices(matrix_a, matrix_b)
        print("Matrix multiplication completed.")

        # Відправлення результату назад клієнту
        client_socket.send(result.tobytes())
        print("Result sent back to client.")
    except Exception as e:
        print(f"Error during client handling: {e}")
        client_socket.send(f"ERROR: {str(e)}".encode('utf-8'))
    finally:
        client_socket.close()
        print("Client connection closed.")

# Основний серверний процес
def start_server(host='0.0.0.0', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Дозволяємо повторно використовувати порт
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    with ThreadPoolExecutor(max_workers=4) as executor:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"New connection accepted from {client_address}")
            executor.submit(handle_client, client_socket)

if __name__ == '__main__':
    start_server()
