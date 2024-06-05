from blog.spam.db import Conexao
import pytest  # type: ignore


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
