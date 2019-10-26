import socket

ADDRESS = socket.gethostname()  # Endereço
PORT = 1234  # Porta
HEADERSIZE = 16  # Define tamanho do header
end = False  # Controla fechamento do cliente

while not end:  # Cliente: Main loop
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria socket TCP cliente (SOCK_STREAM)
    s.connect((ADDRESS, PORT))  # Conecta ao servidor no endereço e porta especificados

    msg = s.recv(64)  # Recebe mensagem do servidor
    msg = msg.decode("utf-8")  # Decodifica mensagem

    fac = input(msg)  # Input do usuário para definir fatorial a ser calculado
    s.send(bytes(fac, "utf-8"))  # Codifica e envia mensagem ao servidor
    # PREPARAÇÂO PARA RECEBER FATORIAL DO SERVIDOR:
    full_msg = ''  # Variável que receberá a mensagem completa
    new_msg = True  # Controle: tem uma nova mensagem?
    end_msg = False  # Controle: é o fim da mensagem?
    msg_len = 0  # Tamanho da mensagem
    while not end_msg:
        msg = s.recv(HEADERSIZE)  # Recebe parte da mensagem
        if new_msg:  # Se a mensagem for nova...
            print(f"new message length: {msg[:HEADERSIZE]}")  # Tamanho da nova mensagem
            msg_len = int(msg[:HEADERSIZE])  # Guarda tamanho da nova mensagem
            new_msg = False  # Nova mensagem = falso. A partir daqui, cliente receberá o resto da mensagem atual

        full_msg += msg.decode(
            "utf-8")  # Decodifica e concatena parte da mensagem atual à variável que guardará a mensagem inteira

        if len(full_msg) - HEADERSIZE == msg_len:  # Se tamanho da mensagem inteira - tamanho do header = tamanho da
            # parte da mensagem...
            print(msg.decode("utf-8"))  # Decodifica e imprime parte da mensagem
            print(full_msg[HEADERSIZE:])  # Imprime mensagem final exceto header
            new_msg = True  #
            full_msg = ''  # Reseta estado das variáveis de controle
            end_msg = True  #

    if fac == "-1":  # Se fatorial a ser calcualdo = -1, fecha o cliente
        print("Aborting...")
        s.close()
        end = True
        break
    else:  # Do contrário...
        opt = input("Another factorial? (Y/n)")  # Calcular outro fatorial?
        if opt.lower() == "y" or opt == "":  # Se sim, programa continua
            pass
        else:  # Do contrário, envia comando de fechamento para o servidor e fecha o cliente
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ADDRESS, PORT))
            s.send(bytes("-1", "utf-8"))
            end = True
            s.close()
