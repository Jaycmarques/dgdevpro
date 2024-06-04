from blog.spam.mail_sender import Sender, EmailNotValid
import pytest

def test_send_mail():
    sender = Sender()
    assert sender is not None

@pytest.mark.parametrize('receiver', ['julio.jcmarques@gmail.com', 'leticiapie@icloud.com'])
def test_receiver(receiver):
    sender = Sender()
    result = sender.send(receiver, 'julionihongo@gmail.com', 'criação enviar email', 'aprendendo a criar testes de spam')

    assert receiver in result

@pytest.mark.parametrize('receiver', ['', 'Julio'])
def test_invalid_receiver(receiver):
    sender = Sender()
    with pytest.raises(EmailNotValid):
        sender.send(receiver, 'julionihongo@gmail.com', 'criação enviar email', 'aprendendo a criar testes de spam')

    

