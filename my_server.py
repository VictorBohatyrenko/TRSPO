
import socket
import struct


def start_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Сервер очікує підключення на {host}:{port}...")
    conn, addr = server_socket.accept()
    print(f"Підключено клієнта: {addr}")

    try:
        for _ in range(100):
            # Отримання повідомлення
            header = conn.recv(4)
            if not header:
                break
            message_length = struct.unpack('!I', header)[0]  # Розпаковка довжини
            message = conn.recv(message_length).decode('utf-8')
            print(f"Отримано: {message}")

            # Формування відповіді
            response = f"Відповідь на: {message}"
            response_bytes = response.encode('utf-8')
            response_header = struct.pack('!I', len(response_bytes))
            conn.sendall(response_header + response_bytes)
    finally:
        conn.close()
        server_socket.close()

if __name__ == "__main__":
    start_server()
