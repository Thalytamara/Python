# Função para adicionar dois números
def adicionar(x, y):
    return x + y

# Função para subtrair dois números
def subtrair(x, y):
    return x - y

# Função para multiplicar dois números
def multiplicar(x, y):
    return x * y

# Função para dividir dois números
def dividir(x, y):
    if y == 0:
        return "Erro: divisão por zero!"
    else:
        return x / y

while True:
    print("\nMenu:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

    opcao = input("Escolha uma opção (1/2/3/4/5): ")

    # Verifica se a entrada é válida
    if opcao not in ['1', '2', '3', '4', '5']:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        continue

    # Converte a entrada para um número inteiro
    opcao = int(opcao)

    # Se a opção for 5, sai do loop
    if opcao == 5:
        print("Obrigado por usar a calculadora. Até mais!")
        break

    # Solicita os números para a operação
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Executa a operação selecionada e mostra o resultado
    if opcao == 1:
        print("Resultado:", adicionar(num1, num2))
    elif opcao == 2:
        print("Resultado:", subtrair(num1, num2))
    elif opcao == 3:
        print("Resultado:", multiplicar(num1, num2))
    elif opcao == 4:
        print("Resultado:", dividir(num1, num2))
