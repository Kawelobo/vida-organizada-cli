tarefas = []

def adicionar():
    tarefa = input("Digite uma tarefa: ")
    if tarefa.strip() == "":
        print("Tarefa inválida!")
        return
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def listar():
    if not tarefas:
        print("Nenhuma tarefa.")
        return
    for i, t in enumerate(tarefas):
        print(f"{i} - {t}")

def menu():
    while True:
        print("\n1-Adicionar  2-Listar  0-Sair")
        op = input("Escolha: ")

        if op == "1":
            adicionar()
        elif op == "2":
            listar()
        elif op == "0":
            break
        else:
            print("Opção inválida")

menu()
