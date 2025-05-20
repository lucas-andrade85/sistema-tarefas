import sqlite3
from database import criar_banco

def adicionar_tarefa(titulo):
    """Adiciona uma nova tarefa ao banco de dados"""
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (titulo) VALUES (?)", (titulo,))
    conn.commit()
    conn.close()
    print(f"✅ Tarefa '{titulo}' adicionada com sucesso!")

def listar_tarefas():
    """Lista todas as tarefas do banco de dados"""
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, concluida FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    
    if not tarefas:
        print("\n📭 Nenhuma tarefa encontrada!")
    else:
        print("\n📋 Lista de Tarefas:")
        for tarefa in tarefas:
            status = "✅" if tarefa[2] else "⏳"
            print(f"{tarefa[0]}. {status} {tarefa[1]}")

def marcar_como_concluida(id_tarefa):
    """Marca uma tarefa como concluída"""
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET concluida = 1 WHERE id = ?", (id_tarefa,))
    conn.commit()
    
    # Verifica se alguma linha foi alterada
    if cursor.rowcount > 0:
        print(f"✅ Tarefa {id_tarefa} marcada como concluída!")
    else:
        print(f"⚠️ Tarefa {id_tarefa} não encontrada!")
    
    conn.close()

def menu():
    """Exibe o menu principal"""
    print("\n" + "="*30)
    print("📝 GERENCIADOR DE TAREFAS")
    print("="*30)
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar como concluída")
    print("4. Sair")

if __name__ == "__main__":
    criar_banco()  # Garante que o banco existe
    
    while True:
        menu()
        opcao = input("\nEscolha uma opção (1-4): ")
        
        if opcao == "1":
            titulo = input("Digite o título da tarefa: ")
            adicionar_tarefa(titulo)
        
        elif opcao == "2":
            listar_tarefas()
        
        elif opcao == "3":
            listar_tarefas()
            try:
                id_tarefa = int(input("\nDigite o ID da tarefa concluída: "))
                marcar_como_concluida(id_tarefa)
            except ValueError:
                print("⚠️ Por favor, digite um número válido!")
        
        elif opcao == "4":
            print("\n👋 Até logo!")
            break
        
        else:
            print("⚠️ Opção inválida! Tente novamente.")