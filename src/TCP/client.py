import socket

HEADERSIZE = 16
end = False

while not end:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))

    msg = s.recv(64)
    msg = msg.decode("utf-8")

    fac = input(msg)
    s.send(bytes(fac, "utf-8"))

    full_msg = ''
    new_msg = True
    end_msg = False
    msg_len = 0
    while not end_msg:
        msg = s.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msg_len = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg.decode("utf-8")

        if len(full_msg) - HEADERSIZE == msg_len:
            print(msg.decode("utf-8"))
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''
            end_msg = True

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
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((socket.gethostname(), 1234))
            s.send(bytes("-1", "utf-8"))
            end = True
            s.close()