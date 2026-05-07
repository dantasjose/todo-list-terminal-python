from todo import Todo


def gerar_proximo_id(tarefas):
    if len(tarefas) == 0:
        return 1
    return max(tarefa.id for tarefa in tarefas) + 1


def adicionar_tarefa(tarefas, nome, descricao, prioridade):
    proximo_id = gerar_proximo_id(tarefas)
    tarefa = Todo(proximo_id, nome, descricao, prioridade)
    tarefas.append(tarefa)
    return tarefa


def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return

    pendentes = [tarefa for tarefa in tarefas if not tarefa.realizado]
    concluidas = [tarefa for tarefa in tarefas if tarefa.realizado]

    print("\n--- TAREFAS PENDENTES ---")
    if len(pendentes) == 0:
        print("Nenhuma tarefa pendente.")
    else:
        for tarefa in pendentes:
            print(tarefa)

    print("\n--- TAREFAS CONCLUÍDAS ---")
    if len(concluidas) == 0:
        print("Nenhuma tarefa concluída.")
    else:
        for tarefa in concluidas:
            print(tarefa)


def buscar_tarefa_por_id(tarefas, id_tarefa):
    for tarefa in tarefas:
        if tarefa.id == id_tarefa:
            return tarefa
    return None


def concluir_tarefa(tarefas, id_tarefa):
    tarefa = buscar_tarefa_por_id(tarefas, id_tarefa)

    if tarefa is None:
        return False

    tarefa.concluir()
    return True


def editar_tarefa(tarefas, id_tarefa, novo_nome, nova_descricao, nova_prioridade):
    tarefa = buscar_tarefa_por_id(tarefas, id_tarefa)

    if tarefa is None:
        return False

    tarefa.editar(novo_nome, nova_descricao, nova_prioridade)
    return True


def remover_tarefa(tarefas, id_tarefa):
    tarefa = buscar_tarefa_por_id(tarefas, id_tarefa)

    if tarefa is None:
        return False

    tarefas.remove(tarefa)
    return True
