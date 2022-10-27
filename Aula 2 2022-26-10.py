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

#estrutura condicional, o famoso if(se)
# se a pessoa for maior de idade, mostre 'você é maior de idade! otimo, ja pode beber ou dirigir'
if idade >= 18:
  print ('você é maior de idade! ótimo, agora pode beber ou dirigir')
else:
  print('você é jovem ainda')

# e se eu quisesse perguntar o genero(M= mascuino e F= feminino)
#mostre o(e você precisa/precisou prestar o serviço militar obrigatorio)
gênero = input(' informe o genero M=masculino, F=feminino, O=outros:')
if idade >= 18 and  gênero == 'M':
  print('e voce tambem precisa/precisou prestar o serviço militar obrigatorio')