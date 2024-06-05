from blog.models import User


def test_save_user(sessao):
    user = User(nome='Julio')
    sessao.salvar(user)
    assert isinstance(user.id, int)


def test_listar_users(sessao):
    users = [User(nome='Julio'), User(nome='Lucas')]
    for user in users:
        sessao.salvar(user)
    assert users == sessao.listar()
