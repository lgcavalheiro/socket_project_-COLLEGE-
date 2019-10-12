import socket

end = False
while not end:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))

    msg = s.recv(1024)
    msg = msg.decode("utf-8")

    fac = input(msg)
    s.send(bytes(fac, "utf-8"))
    msg = s.recv(1024)
    print(msg.decode("utf-8"))

    if fac == "-1":
        print("Aborting...")
        s.close()
        end = True
        break
    else:
        opt = input("Another factorial? (Y/n)")
        if opt.lower() == "y" or opt == "":
            pass
        else:
            s.close()
            end = True
