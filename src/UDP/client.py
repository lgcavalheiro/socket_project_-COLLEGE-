import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

end = False

while not end:
    fac = input("Define factorial:")
    s.sendto(bytes(fac, "utf-8"),(socket.gethostname(), 1234))

    msg, serversocket = s.recvfrom(1234)
    print(msg.decode("utf-8"))

    opt = input("Another factorial? (Y/n)")

    if opt.lower() == "y" or opt == "":
        pass
    else:
        end = True