import sqlite3
from database import criar_banco

def adicionar_tarefa(titulo):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (titulo) VALUES (?)", (titulo,))
    conn.commit()
    conn.close()

def listar_tarefas():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, concluida FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    
    if not tarefas:
        print("Nenhuma tarefa encontrada!")
    else:
        print("\n📋 Suas Tarefas:")
        for tarefa in tarefas:
            status = "✅" if tarefa[2] else "⏳"
            print(f"{tarefa[0]}. {status} {tarefa[1]}")

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
    adicionar_tarefa(titulo)
elif opcao == "2":
    listar_tarefas()