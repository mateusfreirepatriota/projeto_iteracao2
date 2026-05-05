tarefas = []

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nTarefas:")
            for i, t in enumerate(tarefas, 1):
                print(f"{i} - {t}")

    elif opcao == "0":
        break

    else:
        print("Opção inválida")
