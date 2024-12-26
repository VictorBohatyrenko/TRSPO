import socket

def start_server():
    host = '127.0.0.1'  # Локальний хост
    port = 12345        # Порт для зв'язку

    # Створення сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Сервер очікує підключення на {host}:{port}...")
    conn, addr = server_socket.accept()
    print(f"Підключено клієнта: {addr}")

    while True:
        # Отримання повідомлення від клієнта
        client_message = conn.recv(1024).decode('utf-8')
        if client_message.lower() == 'exit':
            print("Клієнт завершив з'єднання.")
            break
        print(f"Клієнт: {client_message}")

        # Відправка відповіді клієнту
        server_message = input("Сервер: ")
        conn.sendall(server_message.encode('utf-8'))
        if server_message.lower() == 'exit':
            print("Сервер завершив з'єднання.")
            break

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
