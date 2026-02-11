nome_alunos = ["Seu Antonio", "Idalguinho", "Fefe", "Uilian", "Eztefania", "Luzkinha", "Rapaizinho de rosa", "Didi", "Leandrin do Gr@u", "Lele"]

for aluno in nome_alunos:
  print(aluno)


veiculos = ["Fusca", "Doublo", "Marea Turbo", "Tiggo", "Uno", "Gol Bolinha", "Chevette", "Monza Tubarão", "Cadete", "Omega", "Virtus", "Opala", "D20", "Celta do Felipe", "Veraneio"]

# Outros carros: Nome do carro + carro legal
# D20, Veraneio e Chevette: Nome do carro + carro clássico

for veiculo in veiculos:

  if veiculo in ("D20", "Veraneio", "Chevette"):
    print(f"{veiculo} carro clássico!")
  else:
    print(f"{veiculo} carro legal!")
