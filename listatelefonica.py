def exibir_menu():
    print("1. Criar contato")
    print("2. Exibir contatos")
    print("3. Sair")

# Inicializando a lista telefônica
agenda_telefonica = {}

# Loop principal do programa
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":  # Criar contato
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o número de telefone: ")
        agenda_telefonica[nome] = telefone
        print("Contato adicionado com sucesso!")

    elif opcao == "2":  # Exibir todos os contatos
        print("Agenda telefonica:")
        for nome, telefone in agenda_telefonica.items():
            print(f"{nome}: {telefone}")

    elif opcao == "3":  # Sair do programa
        print("Saindo...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")