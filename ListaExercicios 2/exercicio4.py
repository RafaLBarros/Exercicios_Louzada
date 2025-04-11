x = input("Digite uma frase: ")

y = x.upper()
print("A quantidade da vogal a na sua frase é:",y.count('A'))
print("A quantidade da vogal a na sua frase é:",y.count('E'))
print("A quantidade da vogal a na sua frase é:",y.count('I'))
print("A quantidade da vogal a na sua frase é:",y.count('O'))
print("A quantidade da vogal a na sua frase é:",y.count('U'))

print("A frase ao contrário é:",x[::-1])

print("A frase com espaços substituidos é:",x.replace(' ','-'))