import socket

ADDRESS = socket.gethostname()  # Endereço
PORT = 1234  # Porta
BUFFER = 4096  # tamanho do buffer

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Cria socket UDP cliente (SOCK_DGRAM)
end = False  # Controle do main loop

while not end:  # Cliente: main loop
    fac = input("Define factorial:")  # Usuário define fatorial a ser calculado
    s.sendto(fac.encode(), (ADDRESS, PORT))  # Cliente envia mensagem codificada para o servidor UDP

    msg, serversocket = s.recvfrom(BUFFER)  # CLiente recebe mensagem e socket do servidor, guarda em variáveis
    print(msg.decode("utf-8"))  # Decodifica e imprime mensagem

    opt = input("Another factorial? (Y/n)").lower()  # Outro fatorial?

    if opt == "y" or opt == "":  # Se sim, programa segue normalmente...
        pass
    else:  # Se não, quebra o main loop
        end = True

s.close()  # Fecha o socket cliente
