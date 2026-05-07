# Todo List Terminal - Versão 1 Simples

Esta é a primeira versão do projeto Todo List desenvolvido em Python.

O objetivo desta versão foi criar uma aplicação simples de terminal para praticar lógica de programação, funções, listas, classes e organização de código em arquivos separados.

## Funcionalidades

- Adicionar tarefas
- Listar tarefas
- Marcar tarefas como concluídas
- Editar tarefas
- Remover tarefas
- Validar entrada do usuário no terminal

## Como funciona

Nesta versão, as tarefas são armazenadas apenas em memória, dentro de uma lista Python.

Isso significa que, ao encerrar o programa, as tarefas cadastradas são perdidas.

Essa limitação foi mantida de propósito, pois a ideia do projeto é mostrar uma evolução gradual.

Na próxima versão, foi adicionada a persistência de dados usando arquivo JSON.

## Estrutura dos arquivos
```
versao_1_simples/
├── main.py
├── todo.py
└── todo_service.py
```

Arquivos
main.py

Arquivo principal da aplicação.

Responsável por exibir o menu, receber as opções do usuário e chamar as funções responsáveis por manipular as tarefas.

todo.py

Arquivo que contém a classe Todo.

Essa classe representa uma tarefa, com informações como:

ID
Nome
Descrição
Status
Prioridade
todo_service.py

Arquivo responsável pelas regras principais da aplicação, como:

adicionar tarefa;
listar tarefas;
concluir tarefa;
editar tarefa;
remover tarefa.
Como executar

No terminal, entre na pasta da versão 1:

cd versao_1_simples

Depois execute:

python main.py
Aprendizados desta versão

Com esta versão, foram praticados conceitos como:

funções;
listas;
classes;
objetos;
laços de repetição;
condicionais;
validação de entrada;
separação de responsabilidades entre arquivos.
Próxima evolução

A próxima versão do projeto adiciona persistência de dados usando JSON, permitindo que as tarefas sejam salvas mesmo após fechar o programa.


