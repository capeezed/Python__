nome = "gabriel"
encontrar = str(input("Digite uma letra: "))

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')