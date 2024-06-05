class Conexao:
    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass


class Sessao:
    count = 0
    users = []

    def salvar(self, user):
        Sessao.count += 1
        user.id = Sessao.count  # type: ignore
        self.users.append(user)

    def listar(self):
        return self.users

    def roll_back(self):
        self.users.clear()

    def fechar(self):
        pass
