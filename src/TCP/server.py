import socket
import math

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
print("Server is up!")

HEADERSIZE = 16
end = False

while not end:
    clientsocket, address = s.accept()

    print("Connection from {} has been made".format(address))

    msg = "Define your factorial (type -1 to abort and close server):"
    print(f'{len(msg):<{HEADERSIZE}}' + msg)

    clientsocket.send(bytes(msg, "utf-8"))
    fac = clientsocket.recv(32)
    fac = int(fac.decode("utf-8"))

    if fac == -1:
        end = True
        print("Server is closing...")
        break
    else:
        fac = "Factorial is: " + str(math.factorial(fac))
        fac = f'{len(fac):<{HEADERSIZE}}' + fac
        print(f'{len(fac):<{HEADERSIZE}}' + fac)
        clientsocket.send(bytes(fac, "utf-8"))
