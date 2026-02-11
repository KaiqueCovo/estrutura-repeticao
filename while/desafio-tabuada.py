'''
Checklist de tarefas

- [x] Pegar número da tabuada atráves do input
- [x] Converter a informação número tabuada para int
- [x] Pegar número de limite atráves do input
- [x] Converter a informação número de limite para int
- [x] Utilizar o while para percorrer e fazer a tabuada
- [x] Criar um contador para meu while (Começo/Start)
- [x] Mostrar mensagem estruturada para o usuário (Ex: 5 x 1 = 5)

- BONUS

- [x] Validar se o numero_tabuada é negativo ou 0
- [x] Validar se o tabuada_limite é negativo ou 0
- [x] Ao final verifique se o usuário deseja gerar outra tabuada
- [] Refatoração do if de validação das variáveis


'''

'''
AND = TODAS CONDIÇÕES DEVEM SER VERDADEIRAS
numero_tabuada < 1 = FALSE
tabuada_limite < 1 = TRUE

OR = UMA DAS CONDIÇÕES PODE SER VERDADEIRA
numero_tabuada < 1 = FALSE
tabuada_limite < 1 = TRUE
'''

while True:

  numero_tabuada = int(input("Digite o número da tabuada: "))
  if numero_tabuada < 1:
    print("Número da tabuada deve ser maior que 0")
    continue # Volta para o começo

  tabuada_limite = int(input("Digite até qual número a tabuada dever ir:"))
  if(tabuada_limite < 1):
    print("Número tabuada e Limite devem ser maior que 0")
    continue # Volta para o começo

  # Estrutura de repetição
  contador = 1
  while contador <= tabuada_limite:
    print(f"{numero_tabuada} x {contador} = {numero_tabuada * contador}") # F-String

    contador += 1

  pergunta = input('Você quer continuar? Digite S ou N').upper()

  if pergunta == 'N':
    print("Estamos encerrando o códiguin!")
    break


  


