import socket
import math

ADDRESS = socket.gethostname()  # Endereço
PORT = 1234  # Porta

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Criação do socket TCP (SOCK_STREAM)
s.bind((ADDRESS, PORT))  # Bind do socket à porta e endereço
s.listen(5)  # Server programado para escutar até 5 clientes diferentes
print("Server is up!")  # AVISO: Server ligado com sucesso

HEADERSIZE = 16  # Definição do tamanho do header
end = False  # Controla fechamento do servidor

while not end:  # Servidor: main loop
    clientsocket, address = s.accept()  # Aceita conexão do cliente, guarda endereço e socket do cliente

    print("Connection from {} has been made".format(address))  # AVISO: Conexão realizada com sucesso

    msg = "Define your factorial (type -1 to abort and close server):"  # Mensagem para o cliente
    print(f'{len(msg):<{HEADERSIZE}}' + msg)  # Imprime tamanho da mensagem + header

    clientsocket.send(bytes(msg, "utf-8"))  # Envia a mensagem codificada para o cliente
    fac = clientsocket.recv(32)  # Recebe mensagem do cliente
    fac = int(fac.decode("utf-8"))  # Decodifica mensagem recebida

    if fac == -1:  # Se mensagem recebida for -1, quebra o main loop e fecha o servidor
        end = True
        print("Server is closing...")
        break
    else:  # Do contrario, processa o fatorial e envia para o cliente
        try:  # Tratamento de exceção
            fac = "Factorial is: " + str(
                math.factorial(fac))  # Forma mensagem a ser enviada ao cliente. Frase + fatorial convertido para string
        except ValueError:  # Erro de valor
            fac = "Value Error: Cannot calculate the factorial of a negative number!"
        fac = f'{len(fac):<{HEADERSIZE}}' + fac  # Adiciona header
        print(f'{len(fac):<{HEADERSIZE}}' + fac)  # Imprime
        clientsocket.send(bytes(fac, "utf-8"))  # Codifica a mensagem e envia ao cliente

s.close()  # Fecha o servidor
