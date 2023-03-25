preco_produto = float(input("Digite o preço do produto: R$"))
desconto = (preco_produto * 5/100)
desconto_aplicado = (preco_produto - desconto)
print("O preço do produto era R$ {}, seu novo preço com 5% de  desconto é R$ {}".format(preco_produto,desconto_aplicado))
