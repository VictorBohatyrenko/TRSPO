# client.py
import socket
import numpy as np
import random

# Функція для генерації матриць
def generate_matrices():
    n, m, l = [random.randint(1001, 1100) for _ in range(3)]
    matrix_a = np.random.rand(n, m)
    matrix_b = np.random.rand(m, l)
    print(f"Generated matrices: A({n},{m}), B({m},{l})")
    return n, m, l, matrix_a, matrix_b

# Клієнтська програма
def client_program(host='127.0.0.1', port=12345):
    n, m, l, matrix_a, matrix_b = generate_matrices()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Відправлення розмірів матриць
    sizes = f"{n},{m},{l}"
    client_socket.send(sizes.encode('utf-8'))
    print("Sent matrix sizes to server.")

    # Відправлення матриць
    data = np.hstack((matrix_a.flatten(), matrix_b.flatten()))
    client_socket.sendall(data.tobytes())
    print("Sent matrix data to server.")

    # Отримання результату
    result_size = n * l * 8
    result_data = bytearray()
    while len(result_data) < result_size:  # Збирання всього результату
        packet = client_socket.recv(1024 * 1024)
        if not packet:
            break
        result_data.extend(packet)

    result_matrix = np.frombuffer(result_data, dtype=np.float64).reshape((n, l))
    print("Result matrix received:")
    print(result_matrix)

    client_socket.close()

if __name__ == '__main__':
    client_program()
