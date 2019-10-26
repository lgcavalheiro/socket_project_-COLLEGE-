import socket
import math

ADDRESS = socket.gethostname()  # Endereço
PORT = 1234  # Porta
BUFFER = 4096  # tamanho do buffer

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Cria socket UDP cliente (SOCK_DGRAM)
s.bind((ADDRESS, PORT))  # Bind do socket à porta e endereço especificados anteriormente

print("Server is up!")  # Mensagem: servidor online

while True:  # Servidor: main loop
    msg, clientsocket = s.recvfrom(BUFFER)  # Recebe mensagem e socket do cliente, guarda em variáveis
    msg = msg.decode("utf-8")  # Decodifica mensagem
    msg = str(math.factorial(int(msg)))  # Calcula fatorial e converte para string
    s.sendto(bytes(msg, "utf-8"), clientsocket)  # Codifica mensagem e envia para o cliente
