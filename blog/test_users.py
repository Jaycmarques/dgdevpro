from blog.db import Conexao
from blog.models import User
import pytest


@pytest.fixture
def conexao():
    conexao_obj = Conexao()
    yield Conexao()
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_save_user(sessao):
    user = User(nome='Julio')
    sessao.salvar(user)
    assert isinstance(user.id, int)


def test_listar_users(sessao):
    users = [User(nome='Julio'), User(nome='Lucas')]
    for user in users:
        sessao.salvar(user)
    assert users == sessao.listar()
