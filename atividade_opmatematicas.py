# Criando Funções para as Operações Matemáticas

# Função para realizar a soma
def soma(a, b):
    return a + b

# Função para realizar a subtração
def subtracao(a, b):
    return a - b

# Função para realizar a multiplicação
def multiplicacao(a, b):
    return a * b

# Função para realizar a divisão
def divisao(a, b):
    # Verifica se o divisor é zero para evitar divisão por zero
    if b == 0:
        return "Erro: divisão por zero!"
    else:
        return a / b


# Função para obter entrada do usuário e realizar operações matemáticas
def operacoes():
    # Obtendo os números do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realizando as operações matemáticas e mostrando os resultados
    print("Soma:", soma(num1, num2))
    print("Subtração:", subtracao(num1, num2))
    print("Multiplicação:", multiplicacao(num1, num2))
    print("Divisão:", divisao(num1, num2))

# Os resultados são mostrados dentro da função operacoes()

# Vamos chamar a função operacoes() para testar o programa
operacoes()
