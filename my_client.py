import socket

def start_client():
    host = '127.0.0.1'  # Локальний хост
    port = 12345        # Порт для зв'язку

    # Створення сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(f"Підключено до сервера на {host}:{port}")

    while True:
        # Відправка повідомлення серверу
        client_message = input("Клієнт: ")
        client_socket.sendall(client_message.encode('utf-8'))
        if client_message.lower() == 'exit':
            print("Клієнт завершив з'єднання.")
            break

        # Отримання відповіді від сервера
        server_message = client_socket.recv(1024).decode('utf-8')
        if server_message.lower() == 'exit':
            print("Сервер завершив з'єднання.")
            break
        print(f"Сервер: {server_message}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
