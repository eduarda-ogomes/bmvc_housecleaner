class Usuario:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def __repr__(self):
        return f"Usuario(id={self.id}, nome='{self.nome}', email='{self.email}')"

    def __str__(self):
        return f"{self.nome} <{self.email}>"