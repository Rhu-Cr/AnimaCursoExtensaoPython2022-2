#comando imput() para permitir que o usuário digite algo
nome = input('digite seu nome:')
#comando de saída...exibir na tela
print(f'Boa noite, seu nome é {nome}')
#exiba, sua idade é...
idade = int(input("Digite sua idade: \n"))
print("Seu nome é "+nome+" e sua idade é "+str(idade))

# e se eu quisesse mostrar o dobro da idade informada
dobro = idade*2
print('o dobro da sua idade é:{}'.format(dobro))

