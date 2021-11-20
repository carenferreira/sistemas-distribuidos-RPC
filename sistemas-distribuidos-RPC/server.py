import socket
import json
from math import factorial

serverPort = 50000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(0)

print("Aguardando conexão de um cliente...")

def soma(number1, number2): 
    return int(number1) + int(number2)

def produto(number1, number2): 
    return int(number1) * int(number2)

def fatorial(number): 
    n = int(number)
    return factorial(n)

def resolveOperacao(dadosJSON):
    if dadosJSON["operacao"] == "soma":
        return soma(dadosJSON["num1"],dadosJSON["num2"])
    
    elif dadosJSON["operacao"] == "produto":
        return produto(dadosJSON["num1"],dadosJSON["num2"])

    elif dadosJSON["operacao"] == "fatorial":
        if dadosJSON["num1"] >= 0:
            return fatorial(dadosJSON["num1"])
    
    return None

while True:
    try:
        conn, addr = serverSocket.accept()
        print("Cliente conectado {}".format(addr))
        message = conn.recv(2048)
        decodedMessage = message.decode('utf-8')
        print("{} ==> {}".format(addr, decodedMessage))

        dadosJSON = json.loads(decodedMessage)
        resposta = resolveOperacao(dadosJSON)
        resposta = str(resposta)
        conn.send(resposta.encode('utf-8'))

        conn.close()
    except ConnectionResetError:
        print(f"Conexão com cliente {addr} perdida")
        conn.close()