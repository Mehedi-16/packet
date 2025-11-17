import socket

HOST = '127.0.0.1'
PORT = 12346

a = input("Enter first number: ")
b = input("Enter second number: ")
op = input("Enter operator (+, -, *, /, %): ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = f"{a} {b} {op}"
client_socket.sendall(message.encode())

result = client_socket.recv(1024).decode()
print("Result:", result)

client_socket.close()
