'''

Tipos de dados - Python

Int = Número Inteiro
Float = Número Quebrados(Flutuantes)
String = Texto
Boolean = Afirmação (TRUE ou FALSE)

List = Lista
Uma coleção de valores que podemos guardar juntos em uma única variável
'''

numerosMegaSena = [4, 8, 32, 35, 46, 58]
mochila = [True, 120.00, False, "Caderno", "Garrafa de água", "Notebook", 18000, "Pastel", "Estilete", "Rapadura"]

compras = ["Abacaxi", "Kiwi", "Arroz", "Goiaba", "Peixe"]

print(compras[0])
print(compras[2])
print(compras[4])


compras.append("Leite")
compras.append("Água Mineral")

compras.remove("Abacaxi")

print()

print(compras)

'''
1. Cada item da lista ocupa uma posição
2. Cada posição tem um número (índice)
3. Dá para pegar o item pela posição

// 5 Items

// 0: Abacaxi
// 1: Kiwi
// 2: Arroz
...
compras = ["Abacaxi", "Kiwi", "Arroz", "Goiaba", "Peixe"]



'''