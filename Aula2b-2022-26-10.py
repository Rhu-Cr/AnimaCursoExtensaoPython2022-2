#pede o nome do aluno e sua nota de (0 a 10) e, se ele tirou 10 mostra '{nome}você é o bixão mesmo...'
nome = input("Informe seu nome: ")
nota = float(input("Digite sua nota de 0 a 10: "))
if nota == 10:
  print (f"{nome}, você é o bichão mermo...")
elif (nota >= 6 and nota < 10):
  print(f'{nome}, bom trabalho')
else:
  print('Burro,não tirou dez')
