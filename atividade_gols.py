# Solicitar o nome do primeiro jogador
nomeA = input("Digite o nome do primeiro jogador: ")

# Solicitar o número de gols do primeiro jogador
resultadoNomeA = int(input("Quantos gols o primeiro jogador fez? "))

# Solicitar o nome do segundo jogador
nomeB = input("Digite o nome do segundo jogador: ")

# Solicitar o número de gols do segundo jogador
resultadoNomeB = int(input("Quantos gols o segundo jogador fez? "))

# Comparar os Resultados e Determinar o Vencedor
# Comparar os gols marcados
if resultadoNomeA > resultadoNomeB:
    print("Vitória de", nomeA)
elif resultadoNomeA < resultadoNomeB:
    print("Vitória de", nomeB)
else:
    print("O jogo deu empate")
