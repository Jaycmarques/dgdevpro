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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('julio@gmail.com', 'Assunto', 'corpo')
    assert len(users) == enviador.qde_email_enviados


def test_parametros_de_spam(sessao):
    user = User(nome='Julio', email='julio@gmail.com')
    sessao.salvar(user)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('lucas@gmail.com', 'Assunto', 'Corpo')
    assert enviador.parametros_de_envios == (
        'lucas@gmail.com',
        'julio@gmail.com',
        'Assunto',
        'Corpo'
    )


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qde_email_enviados = 0
        self.parametros_de_envios = None

    def enviar(self, remetente, enviador, assunto, corpo):
        self.parametros_de_envios = (remetente, enviador, assunto, corpo)
        self.qde_email_enviados += 1
