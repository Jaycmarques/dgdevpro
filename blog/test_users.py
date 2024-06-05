def save_user():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    user = User(nome = 'Julio')
    seesao.salva(user)
    assert isinstance(user.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def listar_users():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    users = [User(nome = 'Julio'), User(nome = 'Lucas')]
    for user in users:
        sessao.salva(users)
    assert users == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()