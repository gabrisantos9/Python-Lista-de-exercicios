preco_produto = float(input("Digite o preço do produto:"))
desconto = (preco_produto * 5/100)
desconto_aplicado = (preco_produto - desconto)
print("Seu novo preço com 5% de  desconto é {}".format(desconto_aplicado))