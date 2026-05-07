class Todo:
    def __init__(self, id, nome, descricao, prioridade, realizado=False):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.prioridade = prioridade
        self.realizado = realizado

    def concluir(self):
        self.realizado = True

    def editar(self, novo_nome, nova_descricao, nova_prioridade):
        self.nome = novo_nome
        self.descricao = nova_descricao
        self.prioridade = nova_prioridade

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "realizado": self.realizado,
        }

    @staticmethod
    def from_dict(dados):
        return Todo(
            dados["id"],
            dados["nome"],
            dados.get("descricao", ""),
            dados.get("prioridade", 1),
            dados.get("realizado", False),
        )

    def __str__(self):
        status = "Concluída" if self.realizado else "Pendente"
        return (
            f"ID: {self.id} | Nome: {self.nome} | "
            f"Descrição: {self.descricao} | Status: {status} | "
            f"Prioridade: {self.prioridade}"
        )
