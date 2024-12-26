
import socket
import struct


def start_client():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Підключено до сервера на {host}:{port}")

    try:
        for i in range(100):
            # Формування повідомлення
            message = f"Повідомлення {i}"
            message_bytes = message.encode('utf-8')
            header = struct.pack('!I', len(message_bytes))  # Довжина повідомлення
            client_socket.sendall(header + message_bytes)

            # Отримання відповіді
            response_header = client_socket.recv(4)
            response_length = struct.unpack('!I', response_header)[0]
            response = client_socket.recv(response_length).decode('utf-8')
            print(f"Сервер відповів: {response}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
