class Todo:
    def __init__(self,id,nome,descricao,prioridade):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.realizado = False
        self.prioridade = prioridade
        
    def __str__(self):
        status = "Concluída" if self.realizado else "Pendente"
        return f"ID: {self.id} | Nome: {self.nome} | Descrição: {self.descricao} | Status: {status} | Prioridade: {self.prioridade}"
    