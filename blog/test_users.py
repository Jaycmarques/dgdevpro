from db import Conexao
from models import User


def save_user():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    user = User(nome='Julio')
    sessao.salvar(user)
    assert isinstance(user.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def listar_users():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    users = [User(nome='Julio'), User(nome='Lucas')]
    for user in users:
        sessao.salvar(users)
    assert users == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
