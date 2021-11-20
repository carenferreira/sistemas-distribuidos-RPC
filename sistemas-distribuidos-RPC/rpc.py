import socket
import json

def conexao(self, args):
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            clientSocket.connect((self.ip, self.port))
            args = json.dumps(args)
            clientSocket.send(args.encode('utf-8'))
            modifiedMessage = clientSocket.recv(1024).decode('utf-8')
            return modifiedMessage
        except Exception as e:
            print(e)
            return None

class OperacoesMatematicas:
    
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def soma(self, num1, num2):
        args = {}
        args ["operacao"] = "soma"
        args ["num1"] = num1
        args ["num2"] = num2    
        return conexao(self, args)
    
    def produto(self, num1, num2):
        args = {}
        args ["operacao"] = "produto"
        args ["num1"] = num1
        args ["num2"] = num2
        return conexao(self, args)

    def fatorial(self, num):
        args = {}
        args ["operacao"] = "fatorial"
        args ["num1"] = num
        return conexao(self, args)
