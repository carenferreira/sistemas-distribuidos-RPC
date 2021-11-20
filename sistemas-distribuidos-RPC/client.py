from rpc import OperacoesMatematicas

RPC_SERVER = "127.0.0.1"
RPC_PORT = 50000

op = OperacoesMatematicas(RPC_SERVER, RPC_PORT)

soma = op.soma(2, 3)
produto = op.produto(4, 5)
fatorial = op.fatorial(6)

print(soma) 
print(produto) 
print(fatorial)