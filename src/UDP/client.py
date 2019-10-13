import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = input("Define mesage:")

s.sendto(bytes(msg, "utf-8"),(socket.gethostname(), 1234))

msg, serversocket = s.recvfrom(1234)

print(msg.decode("utf-8"))
s.close()