from blog.spam.mail_sender import Enviador, EmailNotValid
import pytest  # type: ignore


def test_send_mail():
    sender = Enviador()
    assert sender is not None


@pytest.mark.parametrize('receiver', ['julio.jcmarques@gmail.com', 'leticiapie@icloud.com'])
def test_receiver(receiver):
    sender = Enviador()
    result = sender.enviar(receiver, 'julionihongo@gmail.com', 'criar enviar email', 'aprendendo a criar testes de spam')

    assert receiver in result


@pytest.mark.parametrize('receiver', ['', 'Julio'])
def test_invalid_receiver(receiver):
    sender = Enviador()
    with pytest.raises(EmailNotValid):
        sender.enviar(receiver, 'julionihongo@gmail.com', 'criação enviar email', 'aprendendo a criar testes de spam')
