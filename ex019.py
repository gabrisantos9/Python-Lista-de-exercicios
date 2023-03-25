from random import choice
aluno1 = str(input("Digite o nome do primeiro aluno(a):"))
aluno2 = str(input("Digite o nome do segundo aluno(a):"))
aluno3 = str(input("Digite o nome do quarto aluno(a):"))
aluno4 = str(input("Digite o nome do quarto aluno(a):"))
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista_alunos)
print("O aluno sorteado foi {}".format(escolhido))