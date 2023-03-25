from math import hypot
cateto_oposto = float(input("Digite o cumprimento do cateto oposto:"))
cateto_adjacente = float(input("Digite o cumprimento do cateto adjacente:"))
hipotenusa = hypot(cateto_adjacente, cateto_oposto)
print("A hipotenusa vai medir : {:.2f}".format(hipotenusa))