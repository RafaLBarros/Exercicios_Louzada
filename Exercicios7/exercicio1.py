nome = ""
nota = ""
alunos = {}
while True:
    nome = input("Digite o nome do aluno (-1 para parar): ")
    nota = float(input("Digite a nota do aluno (-1 para parar): "))
    if nome == "-1" or nota == "-1":
        break
    alunos[nome] = nota
for chave, valor in alunos.items():
    print(f"{chave}: {valor}")
