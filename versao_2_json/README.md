# Todo List Terminal - Versão 2

Aplicação simples de lista de tarefas executada pelo terminal.

## Funcionalidades

- Adicionar tarefa
- Listar tarefas pendentes e concluídas separadamente
- Concluir tarefa
- Editar tarefa
- Remover tarefa
- Salvar tarefas em arquivo JSON
- Carregar tarefas salvas ao iniciar o programa

## Estrutura do projeto

```
todo_list_terminal_v2/
├── main.py
├── todo.py
├── todo_service.py
├── storage.py
└── README.md
```

## Como executar

No terminal, dentro da pasta do projeto, execute:

```
python main.py
```

## Sobre o arquivo JSON

As tarefas são salvas automaticamente no arquivo `tarefas.json`.

Esse arquivo é criado quando uma tarefa é adicionada, editada, concluída ou removida.

## Evolução em relação à primeira versão

A primeira versão mantinha as tarefas apenas na memória enquanto o programa estava aberto.

Nesta versão, as tarefas são salvas em um arquivo JSON, permitindo fechar o programa e continuar usando depois sem perder os dados.
