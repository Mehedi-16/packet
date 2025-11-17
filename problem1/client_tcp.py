import socket

filename = "sample.txt"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

with open(filename, 'rb') as f:
    while True:
        chunk = f.read(100)
        if not chunk:
            break
        client_socket.sendall(chunk)
        # acknowledgment এর জন্য অপেক্ষা
        ack = client_socket.recv(1024)
        if ack != b'ACK':
            # যদি ACK না আসে, আবার পাঠাও
            client_socket.sendall(chunk)

print("File sent successfully (TCP).")
client_socket.close()
