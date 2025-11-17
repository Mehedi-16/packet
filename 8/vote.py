import socket
import struct
import threading

GROUP = '224.1.1.1'
PORT = 12346
TOTAL = 5
votes = []
done = threading.Event()

def receive(sock):
    while True:
        data, _ = sock.recvfrom(1024)
        msg = data.decode().upper()


        if msg.startswith("RESULT:"):
            print("\nFinal Result Received:\n", msg[7:])
            done.set()
            break

      
        if msg in ['A','B']:
            votes.append(msg)
            print("Got:", msg)
            if len(votes) == TOTAL:
             
                final = make_result()
                sock.sendto(("RESULT:" + final).encode(), (GROUP, PORT))
                done.set()
                break

def make_result():
    a = votes.count('A')
    b = votes.count('B')
    result = f"A = {a} \n B = {b} \n"
    if a > b:
        result += "Winner: A"
    elif b > a:
        result += "Winner: B"
    else:
        result += "Tie"
    return result


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1) 
s.bind(('', PORT))


mreq = struct.pack("4sl", socket.inet_aton(GROUP), socket.INADDR_ANY)
s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


threading.Thread(target=receive, args=(s,), daemon=True).start()


vote = input("Vote (A/B): ").upper()
if vote in ['A','B']:
    s.sendto(vote.encode(), (GROUP, PORT))
    print("Vote sent")
else:
    print("Invalid vote")


done.wait()
s.close()
