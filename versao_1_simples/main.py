from todo_service import adicionar_tarefa, listar_tarefas,concluir_tarefa, editar_tarefa, remover_tarefa

def ler_opcao_menu():
    while True:
        print("\n--- MENU TODO LIST ---")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Editar tarefa")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao in ["1", "2", "3", "4", "5", "0"]:
            return opcao
        else:
            print("Opção inválida. Escolha 1, 2, 3, 4, 5, ou 0.")
            
def ler_nome():
    while True:
        nome = input("Digite o nome da tarefa: ").strip()
        
        if nome != "":
            return nome
        else:
            print("O nome da tarefa não pode ficar vazio.")
            
def ler_prioridade():
    while True:
        entrada = input("Digita a prioridade da tarefa (1, 2 ou 3): ").strip()
        
        if entrada in ["1", "2", "3"]:
            return int(entrada)
        else:
            print("Prioridade inválida. Digite apenas 1, 2, ou 3.")
            
def ler_id_tarefa():
    while True:
      entrada = input("Digite o ID da tarefa: ").strip()
    
      if entrada.isdigit():
        return int(entrada)
      else:
        print("ID inválido. Digite apenas números inteiros positivos.")            
            
tarefas = []
proximo_id = 1

while True:
    opcao = ler_opcao_menu()
    
    if opcao == "1":
        nome = ler_nome()
        descricao = input("Digite a descrição da tarefa: ").strip()
        prioridade = ler_prioridade()
        
        proximo_id = adicionar_tarefa(
            tarefas,
            proximo_id,
            nome,
            descricao,
            prioridade
        )
        
        print("Tarefa adicionada com sucesso!")
    elif opcao == "2":
        listar_tarefas(tarefas)
    
    elif opcao == "3":
        id_tarefa = ler_id_tarefa()
        sucesso = concluir_tarefa (tarefas, id_tarefa)
        
        if sucesso:
            print("Tarefa concluída com sucesso!")
        else:
            print("Tarefa não encontrada.")   
            
    elif opcao == "4":
        id_tarefa = ler_id_tarefa()
        novo_nome = ler_nome()
        nova_descricao = input("Digite a nova descrição da tarefa: ").strip()
        nova_prioridade = ler_prioridade()
        sucesso = editar_tarefa(
            tarefas,
            id_tarefa,
            novo_nome,
            nova_descricao,
            nova_prioridade
        )
        if sucesso:
            print("Tarefa editada com sucesso!")
        else:
            print("Tarefa não encontrada.")
            
    elif opcao == "5":
      id_tarefa = ler_id_tarefa()
      sucesso = remover_tarefa(tarefas, id_tarefa)   
    
      if sucesso:
        print("Tarefa removida com sucesso!") 
      else:
        print("Tarefa não encontrada.")            
                     
        
    elif opcao == "0":
        print("Encerrando o programa...")
        break
                                        
                        