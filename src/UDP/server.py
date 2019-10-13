import socket
import math

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((socket.gethostname(), 1234))

print("Server is up!")

while True:
    msg, clientsocket = s.recvfrom(1234)
    msg = msg.decode("utf-8")
    msg = str(math.factorial(int(msg)))
    s.sendto(bytes(msg, "utf-8"), clientsocket)
