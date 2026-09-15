tarefas = []

print("=== LISTA DE TAREFAS ===")

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append({"nome": tarefa, "concluida": False})
        print("Tarefa adicionada!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(tarefas):
                status = "✓" if tarefa["concluida"] else " "
                print(f"{i + 1}. [{status}] {tarefa['nome']}")

    elif opcao == "3":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            numero = int(input("Digite o número da tarefa concluída: "))
            if 1 <= numero <= len(tarefas):
                tarefas[numero - 1]["concluida"] = True
                print("Tarefa concluída!")
            else:
                print("Número inválido.")

    elif opcao == "4":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            numero = int(input("Digite o número da tarefa que deseja remover: "))
            if 1 <= numero <= len(tarefas):
                tarefas.pop(numero - 1)
                print("Tarefa removida!")
            else:
                print("Número inválido.")

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
print("projeto desenvolvido em Python")
