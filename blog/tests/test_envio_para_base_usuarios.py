from unittest.mock import Mock
from blog.spam.mail_sender import Enviador
from blog.spam.main import EnviadorDeSpam
from blog.models import User
import pytest


@pytest.mark.parametrize(
        'users',
        [
            [
                User(nome='Julio', email='julio@gmail.com'),
                User(nome='Lucas', email='lucas@gmail.com')
            ],
            [
                User(nome='Julio', email='julio@gmail.com')
            ]
        ]
)
def test_qde_de_spam(sessao, users):
    for user in users:
        sessao.salvar(user)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('julio@gmail.com', 'Assunto', 'corpo')
    assert len(users) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    user = User(nome='Julio', email='julio@gmail.com')
    sessao.salvar(user)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('lucas@gmail.com', 'Assunto', 'Corpo')
    enviador.enviar.assert_called_once_with(
        'lucas@gmail.com',
        'julio@gmail.com',
        'Assunto',
        'Corpo'
    )
