alunos = int(input("Quantos alunos tem na sua academia: "))
quant = soma = 0
while quant < alunos:
    peso = float(input("Digite o peso(Kg) do {}ª aluno: ".format(quant + 1)))
    soma += peso
    quant += 1
media = soma / quant
print("A media de peso dos alunos equivale á {}".format(media))
