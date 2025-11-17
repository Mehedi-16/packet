import socket, struct, threading

GROUP = '224.1.1.1'
PORT  = 12346

# message receive করার ফাংশন
def receive(sock):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            msg = data.decode()

            # sender + message print (easy style)
            print("\nFrom " + addr[0] + ":" + str(addr[1]) + " → " + msg)

            # prompt দেখাও
            print("You: ")
        except:
            break


# socket setup
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', PORT))

# multicast group join
mreq = struct.pack("4sl", socket.inet_aton(GROUP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print("Multicast Chat started")
print("Group: " + GROUP + ":" + str(PORT) + "\n")

# receiver thread চালু
threading.Thread(target=receive, args=(sock,), daemon=True).start()

# নিজের message পাঠানো
try:
    while True:
        msg = input("You: ")
        sock.sendto(msg.encode(), (GROUP, PORT))
except KeyboardInterrupt:
    print("\nChat ended")

sock.close()
