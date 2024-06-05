class Conexao:
    def gerar_sessao():
        return Sessao()
    
    def fechar(self):
        pass 

class Sessao:
    count = 0
    users = []
    def salvar(self, user):
        Sessao.count += 1
        user.id = Sessao.count
        self.users.append(user)
    
    def listar(self):
        return self.users
    
    def roll_back(self):
        pass

    def fechar(self):
        pass