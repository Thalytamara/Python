def exibir_menu():
    print("1. Adicionar tarefa")
    print("2. Listar todas as tarefas")
    print("3. Encerrar")

# Inicializando a lista de tarefas
lista_tarefas = []

# Loop principal do programa
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":  # Adicionar tarefa
        tarefa = input("Digite a descrição da tarefa: ")
        lista_tarefas.append({"descricao": tarefa, "concluida": False})
        print("Tarefa adicionada com sucesso! \n")

    elif opcao == "2":  # Listar todas as tarefas
        if not lista_tarefas:
            print("A lista de tarefas está vazia. \n")
        else:
            print("Tarefas: \n")
            for i, tarefa in enumerate(lista_tarefas):
                print(f"{i + 1}. {tarefa['descricao']}\n")

    elif opcao == "3":  # Sair do programa
        print("Encerrando...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")