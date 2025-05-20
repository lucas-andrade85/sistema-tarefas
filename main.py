from database import criar_banco

def menu():
    print("\n📝 Gerenciador de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Sair")

if __name__ == "__main__":
    criar_banco()
    while True:
        menu()
        opcao = input("Escolha: ")
        
        if opcao == "1":
            titulo = input("Título da tarefa: ")
            print(f"Tarefa '{titulo}' adicionada!")
        elif opcao == "2":
            print("Lista de tarefas aparecerá aqui")
        elif opcao == "3":
            break