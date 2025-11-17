import socket

def calculate(a, b, op):
    a, b = int(a), int(b)
    if op == '+': return str(a + b)
    elif op == '-': return str(a - b)
    elif op == '*': return str(a * b)
    elif op == '/': return str(a // b) 
    elif op == '%': return str(a % b)
    else: return "Invalid operator"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost',12346))
server_socket.listen(5)

while True:
    conn, addr = server_socket.accept()
    data = conn.recv(1024).decode()
    a, b, op = data.split()
    result = calculate(a, b, op)
    conn.sendall(result.encode())
    conn.close()
