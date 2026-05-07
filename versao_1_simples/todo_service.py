from todo import Todo

def adicionar_tarefa(tarefas, proximo_id, nome, descricao, prioridade):
    tarefa = Todo(proximo_id, nome, descricao, prioridade)
    tarefas.append(tarefa)
    return proximo_id + 1

def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        for tarefa in tarefas:
            print(tarefa)    

def buscar_tarefas_por_id(tarefas, id):
    for tarefa in tarefas:
        if tarefa.id == id:
            return tarefa
    return None 
   
def concluir_tarefa(tarefas,id):
    tarefa = buscar_tarefas_por_id(tarefas, id)
    
    if tarefa is not None:
        tarefa.realizado= True
        return True
    else:
        return False                    
    
def editar_tarefa(tarefas,id,novo_nome, nova_descricao, nova_prioridade):
    tarefa = buscar_tarefas_por_id(tarefas, id)
    
    if tarefa is not None:
        tarefa.nome = novo_nome
        tarefa.descricao = nova_descricao
        tarefa.prioridade = nova_prioridade
        return True
    else:
        return False
    
def remover_tarefa(tarefas, id):
    tarefa = buscar_tarefas_por_id(tarefa, id)
    
    if tarefa is not None:
        tarefas.remove(tarefa)
        return True
    else:
        return False        