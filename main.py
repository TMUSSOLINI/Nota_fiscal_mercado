from produto import Produto

carrinho = []
print("*********** Mercado do Thiago ************")
print("Seja bem vindo!! insira o produto no carrinho: ")

nome = input("Qual o nome do produto: ")
marca = input("Qual a marca do produto: ")
preco = float(input("Qual o preco: "))
quantidade = int(input("Qual a quantidade: "))

produto = Produto(nome, marca, preco, quantidade)
carrinho.append(produto.extrato())

options = input("Deseja Encerrar a compra? (y/n) ")

while options == 'n':
    nome = input("Qual o nome do produto: ")
    marca = input("Qual a marca do produto: ")
    preco = float(input("Qual o preco: "))
    quantidade = int(input("Qual a quantidade: "))
    produto = Produto(nome, marca, preco, quantidade)
    carrinho.append(produto.extrato())
    options = input("Deseja Encerrar a compra? (y/n) ")

total = 0
for name, qtde, valor in carrinho:
    print(f"{name}   {qtde}un   R${format(valor, '.2f')}")
    print('----------------------')
    total += qtde * valor

print(f'TOTAL:   R${format(total, ".2f")}')
