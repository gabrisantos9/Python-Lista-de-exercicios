salario = float(input("Digite o seu salario: R$"))
aumento = float(salario * 15/100)
aumento_salario = (salario + aumento)
print("Seu salário era : R$ {}, seu novo salário com 15% de aumento é : R$ {}".format(salario, aumento_salario))