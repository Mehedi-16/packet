import socket

filename = "sample.txt"
server_address = ('localhost', 12345)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with open(filename, 'rb') as f:
    while True:
        chunk = f.read(100)
        if not chunk:
            break
        client_socket.sendto(chunk, server_address)

# ফাইল শেষ হলে special message পাঠাও
client_socket.sendto(b'EOF', server_address)

print("File sent successfully.")
client_socket.close()
