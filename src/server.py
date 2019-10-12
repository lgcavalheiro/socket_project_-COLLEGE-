import socket
import math

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

end = False
while not end:
    clientsocket, address = s.accept()

    print("Connection from {} has been made".format(address))

    clientsocket.send(bytes("Define your factorial (type -1 to abort and close server):", "utf-8"))
    fac = clientsocket.recv(1024)
    fac = int(fac.decode("utf-8"))

    if fac == -1:
        end = True
        print("Server is closing...")
        clientsocket.send(bytes("Server is closing...", "utf-8"))
        break
    else:
        fac = str(math.factorial(fac))
        clientsocket.send(bytes("Factorial is: " + fac, "utf-8"))
        clientsocket.close()
