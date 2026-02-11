'''

O que é uma estrutura de repetição?

-> Serve para executar um bloco de código várias vezes
-> ENQUANTO UMA CONDIÇÃO FOR VERDADEIRA

'''

# Quero fazer uma contagem de 10 ATÉ 0 (DECRESCENTE)

'''
Qual a lógica de uma tabuada? Quero fazer a tabuada do 5
e deve mostrar 

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
....

'''


# Tabuada do 5

tabuada = 5
contador = 0

while contador <= 10:
  # 5 x 1 = 5
  print(tabuada, " x ", contador, " = ", contador * tabuada )
  contador += 1

