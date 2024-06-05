from blog.db import Conexao
from blog.models import User


def test_save_user():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    user = User(nome='Julio')
    sessao.salvar(user)
    assert isinstance(user.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def test_listar_users():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    users = [User(nome='Julio'), User(nome='Lucas')]
    for user in users:
        sessao.salvar(user)
    assert users == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
