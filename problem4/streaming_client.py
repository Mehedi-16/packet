import socket

# UDP socket তৈরি
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12346)

# Filename পাঠানো
filename = input("Enter media filename: ")
client_socket.sendto(filename.encode(), server_address)

with open("received_" + filename, 'wb') as f:
    total_bytes = 0
    while True:
        try:
            data, _ = client_socket.recvfrom(2048)
            if not data:
                break
            f.write(data)
            total_bytes += len(data)

            # Reasonable amount আসলে playback শুরু (simulate)
            if total_bytes > 5000:  # 5KB threshold
                print("Launching media player...")
                break
        except:
            break

print("Streaming complete.")
client_socket.close()
