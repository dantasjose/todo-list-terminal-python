import json
from pathlib import Path
from todo import Todo

ARQUIVO_TAREFAS = Path("tarefas.json")


def carregar_tarefas():
    if not ARQUIVO_TAREFAS.exists():
        return []

    with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return [Todo.from_dict(item) for item in dados]


def salvar_tarefas(tarefas):
    dados = [tarefa.to_dict() for tarefa in tarefas]

    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
